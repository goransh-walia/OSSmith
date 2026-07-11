"""SQLAlchemy ORM models.

Empty as of Sprint 2 ("Core Platform"). No domain models exist yet —
this package exists so the database layer (`app/database/`) and
Alembic migrations are fully wired ahead of the first model.

When the first model is added, it must:
    1. Inherit from `app.database.base.Base`.
    2. Be imported in this file's `__init__.py` (or a central registry)
       so Alembic's autogenerate can discover it.
"""
