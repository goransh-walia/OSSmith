"""Version endpoint.

Returns the project name and current application version, sourced
from `Settings` rather than hardcoded, so it can never drift from
`app/core/config.py`.
"""

from fastapi import APIRouter

from app.api.v1.dependencies import SettingsDep
from app.schemas.common import VersionResponse

router = APIRouter(tags=["Operational"])


@router.get(
    "/version",
    response_model=VersionResponse,
    summary="Application version",
    description="Returns the project name and current application version.",
)
def get_version(settings: SettingsDep) -> VersionResponse:
    """Return the project name and version from application settings."""
    return VersionResponse(project=settings.PROJECT_NAME, version=settings.VERSION)
