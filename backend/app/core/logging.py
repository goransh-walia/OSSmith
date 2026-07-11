"""Structured logging configuration.

OSSmith uses `structlog` for structured, machine-parseable logging.
In development, logs are rendered as human-readable colored console
output. In production, logs are rendered as JSON lines suitable for
ingestion by log aggregation tools.

This module also provides `RequestLoggingMiddleware`, which logs every
request with method, path, status code, and latency.
"""

from __future__ import annotations

import logging
import sys
import time
import uuid
from collections.abc import Awaitable, Callable

import structlog
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from structlog.types import EventDict, Processor

from app.core.config import Settings

logger = structlog.get_logger("ossmith")


def _drop_color_message_key(_: object, __: str, event_dict: EventDict) -> EventDict:
    """Remove the `color_message` key injected by stdlib logging integration.

    It duplicates `event` and is only useful for human-readable console
    rendering, which structlog's own renderer already handles.
    """
    event_dict.pop("color_message", None)
    return event_dict


def configure_logging(settings: Settings) -> None:
    """Configure structlog and the stdlib logging module.

    Must be called once, during application startup, before any
    logger is used. See `app.core.lifespan`.
    """
    shared_processors: list[Processor] = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.StackInfoRenderer(),
        _drop_color_message_key,
    ]

    processors: list[Processor]
    if settings.is_production:
        # Production: single-line JSON, safe for log aggregators.
        processors = [
            *shared_processors,
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer(),
        ]
    else:
        # Development: human-readable, colorized console output.
        processors = [
            *shared_processors,
            structlog.dev.ConsoleRenderer(colors=True),
        ]

    structlog.configure(
        processors=processors,
        wrapper_class=structlog.make_filtering_bound_logger(
            logging.getLevelNamesMapping()[settings.LOG_LEVEL.upper()]
        ),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(file=sys.stdout),
        cache_logger_on_first_use=True,
    )


class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Logs every HTTP request with method, path, status, and latency.

    A `request_id` is generated per request and attached to the log
    context, making it possible to correlate every log line emitted
    while handling a single request.
    """

    async def dispatch(
        self,
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        request_id = str(uuid.uuid4())
        request.state.request_id = request_id
        start_time = time.perf_counter()

        structlog.contextvars.bind_contextvars(request_id=request_id)

        try:
            response = await call_next(request)
        except Exception:
            duration_ms = round((time.perf_counter() - start_time) * 1000, 2)
            logger.exception(
                "request_failed",
                method=request.method,
                path=request.url.path,
                duration_ms=duration_ms,
            )
            raise
        else:
            duration_ms = round((time.perf_counter() - start_time) * 1000, 2)
            log_method = logger.info if response.status_code < 500 else logger.error
            log_method(
                "request_completed",
                method=request.method,
                path=request.url.path,
                status_code=response.status_code,
                duration_ms=duration_ms,
            )
            response.headers["X-Request-ID"] = request_id
            return response
        finally:
            structlog.contextvars.unbind_contextvars("request_id")
