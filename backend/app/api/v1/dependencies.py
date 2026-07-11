"""Shared FastAPI dependencies for the v1 API.

Route-level dependencies (things every route in `v1` might need) are
defined here. Endpoint-specific dependencies belong next to the
endpoint that uses them.
"""

from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.core.config import Settings, get_settings
from app.database.session import get_db

SettingsDep = Annotated[Settings, Depends(get_settings)]
"""Injects the cached application `Settings`."""

DbSessionDep = Annotated[Session, Depends(get_db)]
"""Injects a request-scoped database `Session`."""
