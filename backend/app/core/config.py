"""Application configuration.

All runtime configuration flows through a single `Settings` object,
populated from environment variables (and a local `.env` file in
development). No other module should read `os.environ` directly —
if a new value needs to be configurable, it belongs here.

Usage:
    from app.core.config import get_settings

    settings = get_settings()
"""

from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Strongly-typed application settings.

    Values are read from environment variables first, falling back to
    a `.env` file (see `.env.example`), and finally to the defaults
    declared below. Defaults are safe for local development only —
    every deployed environment is expected to override them explicitly.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # --- Project metadata -------------------------------------------------
    PROJECT_NAME: str = Field(
        default="OSSmith",
        description="Human-readable project name, used in API metadata.",
    )
    VERSION: str = Field(
        default="0.2.0-alpha",
        description="Current application version, exposed via /version.",
    )

    # --- Runtime environment -----------------------------------------------
    ENVIRONMENT: Literal["development", "staging", "production", "test"] = Field(
        default="development",
        description="Deployment environment. Controls logging format and docs exposure.",
    )
    DEBUG: bool = Field(
        default=True,
        description="Enables verbose logging and permissive error responses.",
    )

    # --- Server --------------------------------------------------------------
    HOST: str = Field(default="0.0.0.0", description="Bind host for the ASGI server.")
    PORT: int = Field(default=8000, description="Bind port for the ASGI server.")

    # --- Logging -------------------------------------------------------------
    LOG_LEVEL: Literal["debug", "info", "warning", "error", "critical"] = Field(
        default="info",
        description="Minimum log level emitted by the application logger.",
    )

    # --- Database --------------------------------------------------------------
    DATABASE_URL: str = Field(
        default="sqlite:///./ossmith.db",
        description=(
            "SQLAlchemy database URL. Defaults to a local SQLite file so the "
            "project runs with zero external dependencies out of the box."
        ),
    )

    # --- API -------------------------------------------------------------------
    API_V1_PREFIX: str = Field(
        default="",
        description=(
            "Path prefix for versioned API routes. Left empty in Sprint 2 so "
            "operational endpoints (/, /health, /version) remain unversioned; "
            "future business endpoints can set this to '/api/v1'."
        ),
    )

    @property
    def is_production(self) -> bool:
        """Whether the application is running in production."""
        return self.ENVIRONMENT == "production"

    @property
    def is_testing(self) -> bool:
        """Whether the application is running under the test suite."""
        return self.ENVIRONMENT == "test"


@lru_cache
def get_settings() -> Settings:
    """Return the cached application settings instance.

    `lru_cache` ensures the environment is only parsed once per process,
    and lets FastAPI dependencies (`Depends(get_settings)`) reuse the
    same instance without re-reading the environment on every request.
    """
    return Settings()
