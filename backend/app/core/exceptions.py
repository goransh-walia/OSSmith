"""Centralized error handling.

FastAPI's default error responses (plain `{"detail": "..."}` for
`HTTPException`, raw tracebacks for unhandled exceptions) are
inconsistent and leak implementation details. This module defines a
single JSON error shape and registers handlers that guarantee every
error response — expected or not — follows it.

Response shape:
    {
        "error": {
            "code": "not_found",
            "message": "The requested resource was not found.",
            "request_id": "b3b3c3e0-..."
        }
    }
"""

from __future__ import annotations

import structlog
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

logger = structlog.get_logger("ossmith")


class OSSmithError(Exception):
    """Base class for application-raised errors.

    Services and repositories should raise subclasses of this instead
    of generic `Exception` or FastAPI's `HTTPException`, keeping the
    business logic layer decoupled from the web framework.
    """

    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    code: str = "internal_error"

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class NotFoundError(OSSmithError):
    """Raised when a requested resource does not exist."""

    status_code = status.HTTP_404_NOT_FOUND
    code = "not_found"


def _error_response(
    request: Request,
    status_code: int,
    code: str,
    message: str,
    details: list[dict[str, object]] | None = None,
) -> JSONResponse:
    request_id = getattr(request.state, "request_id", None)
    error_body: dict[str, object] = {
        "code": code,
        "message": message,
        "request_id": request_id,
    }
    if details:
        error_body["details"] = details
    return JSONResponse(status_code=status_code, content={"error": error_body})


def register_exception_handlers(app: FastAPI) -> None:
    """Register all centralized exception handlers on the FastAPI app."""

    @app.exception_handler(OSSmithError)
    async def handle_ossmith_error(request: Request, exc: OSSmithError) -> JSONResponse:
        logger.warning("application_error", code=exc.code, message=exc.message)
        return _error_response(request, exc.status_code, exc.code, exc.message)

    @app.exception_handler(StarletteHTTPException)
    async def handle_http_exception(request: Request, exc: StarletteHTTPException) -> JSONResponse:
        return _error_response(
            request,
            exc.status_code,
            code="http_error",
            message=str(exc.detail),
        )

    @app.exception_handler(RequestValidationError)
    async def handle_validation_error(
        request: Request, exc: RequestValidationError
    ) -> JSONResponse:
        return _error_response(
            request,
            status.HTTP_422_UNPROCESSABLE_ENTITY,
            code="validation_error",
            message="The request could not be validated. See `details` for more information.",
            details=[
                {"field": ".".join(str(p) for p in err["loc"]), "message": err["msg"]}
                for err in exc.errors()
            ],
        )

    @app.exception_handler(Exception)
    async def handle_unhandled_exception(request: Request, exc: Exception) -> JSONResponse:
        logger.exception("unhandled_exception")
        return _error_response(
            request,
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            code="internal_error",
            message="An unexpected error occurred.",
        )
