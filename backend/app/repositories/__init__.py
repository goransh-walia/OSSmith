"""Persistence layer: repositories.

Repositories are the only part of the application allowed to issue
SQLAlchemy queries. Services depend on repositories; routes never
touch a repository (or the database session) directly.

Empty as of Sprint 2 — there are no models to persist yet. The
convention for future repositories:

    class ThingRepository:
        def __init__(self, db: Session) -> None:
            self._db = db

        def get(self, thing_id: int) -> Thing | None: ...
        def list(self) -> list[Thing]: ...
        def create(self, thing: Thing) -> Thing: ...
"""
