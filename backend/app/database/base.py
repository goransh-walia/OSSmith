"""Declarative base for all SQLAlchemy ORM models.

Every model defined in `app/models/` must inherit from `Base`. Keeping
the base in its own module (rather than defining it alongside the
first model) avoids circular imports between `models/` and `alembic/`.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """Base class for all ORM models in the application."""
