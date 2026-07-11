"""Application lifespan management.

Startup and shutdown behavior is defined here, using FastAPI's
`lifespan` context manager rather than the deprecated
`@app.on_event` decorators.
"""

from __future__ import annotations

import time
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

import structlog
from fastapi import FastAPI

from app.core.config import get_settings
from app.core.logging import configure_logging
from app.database.session import dispose_engine

logger = structlog.get_logger("ossmith")


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Manage startup and shutdown for the OSSmith API.

    Startup:
        - Configure structured logging
        - Log a startup event with key configuration

    Shutdown:
        - Dispose of the database engine's connection pool
        - Log a shutdown event
    """
    settings = get_settings()
    configure_logging(settings)

    start_time = time.perf_counter()
    logger.info(
        "startup",
        project=settings.PROJECT_NAME,
        version=settings.VERSION,
        environment=settings.ENVIRONMENT,
    )

    yield

    dispose_engine()
    uptime_seconds = round(time.perf_counter() - start_time, 2)
    logger.info("shutdown", uptime_seconds=uptime_seconds)
