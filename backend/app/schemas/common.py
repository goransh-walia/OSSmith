"""Response schemas for the operational endpoints (`/`, `/health`, `/version`)."""

from pydantic import BaseModel, ConfigDict, Field


class RootResponse(BaseModel):
    """Response body for `GET /`."""

    model_config = ConfigDict(json_schema_extra={"example": {"message": "Welcome to OSSmith API"}})

    message: str = Field(..., description="A friendly welcome message.")


class HealthResponse(BaseModel):
    """Response body for `GET /health`."""

    model_config = ConfigDict(json_schema_extra={"example": {"status": "healthy"}})

    status: str = Field(..., description="Current health status of the service.")


class VersionResponse(BaseModel):
    """Response body for `GET /version`."""

    model_config = ConfigDict(
        json_schema_extra={"example": {"project": "OSSmith", "version": "0.2.0-alpha"}}
    )

    project: str = Field(..., description="Project name.")
    version: str = Field(..., description="Current application version.")
