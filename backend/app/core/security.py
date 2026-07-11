"""Security configuration.

Sprint 2 deliberately does not implement authentication or
authorization — see `ROADMAP.md`. This module provides the security
primitives that *are* in scope for a production-grade API foundation:

- CORS configuration
- Baseline security response headers

Future sprints introducing authentication (JWT/OAuth against GitHub)
should extend this module rather than scattering security concerns
elsewhere.
"""

from __future__ import annotations

from collections.abc import Awaitable, Callable

from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import Response

from app.core.config import Settings

# Security headers applied to every response. Values are conservative
# defaults appropriate for a JSON API with no server-rendered HTML.
_SECURITY_HEADERS: dict[str, str] = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "no-referrer",
    "Permissions-Policy": "geolocation=(), microphone=(), camera=()",
}


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Attaches baseline security headers to every response."""

    async def dispatch(
        self,
        request: Request,
        call_next: Callable[[Request], Awaitable[Response]],
    ) -> Response:
        response = await call_next(request)
        for header, value in _SECURITY_HEADERS.items():
            response.headers.setdefault(header, value)
        return response


def configure_security(app: FastAPI, settings: Settings) -> None:
    """Attach CORS and security-header middleware to the application.

    CORS origins are permissive in development to simplify local
    frontend work, and are expected to be locked down via environment
    configuration before any production deployment.
    """
    allowed_origins = ["*"] if not settings.is_production else []

    app.add_middleware(
        CORSMiddleware,
        allow_origins=allowed_origins,
        allow_credentials=False,
        allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
        allow_headers=["*"],
    )
    app.add_middleware(SecurityHeadersMiddleware)
