"""Database engine and session management.

Provides a single, process-wide `Engine` and a `sessionmaker` used to
create request-scoped sessions via the `get_db` FastAPI dependency.

Sprint 2 wires this up completely (engine, session, Alembic) with no
models yet — the first model added in a future sprint should require
no changes here.
"""

from __future__ import annotations

from collections.abc import Generator

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import get_settings

settings = get_settings()

# `check_same_thread` is only relevant for SQLite; it's a no-op for
# other database backends and is harmless to pass unconditionally
# when the URL indicates SQLite.
_connect_args = {"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {}

engine: Engine = create_engine(
    settings.DATABASE_URL,
    connect_args=_connect_args,
    pool_pre_ping=True,
)

SessionLocal: sessionmaker[Session] = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)


def get_db() -> Generator[Session, None, None]:
    """FastAPI dependency yielding a request-scoped database session.

    The session is always closed at the end of the request, even if
    an exception is raised while handling it.

    Usage:
        @router.get("/things")
        def list_things(db: Session = Depends(get_db)) -> list[Thing]:
            ...
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def dispose_engine() -> None:
    """Dispose of the engine's connection pool.

    Called during application shutdown (see `app.core.lifespan`) to
    release database connections cleanly.
    """
    engine.dispose()
