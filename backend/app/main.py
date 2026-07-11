"""OSSmith API application entrypoint.

Run locally with:
    uvicorn app.main:app --reload

The application is assembled with a factory function (`create_app`)
rather than a bare module-level `FastAPI()` instance, so tests can
construct isolated app instances with different settings if needed.
"""

from fastapi import APIRouter, FastAPI

from app.api.v1.router import api_router
from app.core.config import get_settings
from app.core.exceptions import register_exception_handlers
from app.core.lifespan import lifespan
from app.core.logging import RequestLoggingMiddleware
from app.core.security import configure_security
from app.schemas.common import RootResponse


def create_app() -> FastAPI:
    """Construct and configure the FastAPI application instance."""
    settings = get_settings()

    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description=(
            "OSSmith is an AI-powered mentor that teaches developers how to "
            "become excellent open-source contributors. This API is the "
            "platform's backend — see https://github.com/<org>/OSSmith for "
            "the full project."
        ),
        lifespan=lifespan,
    )

    configure_security(app, settings)
    app.add_middleware(RequestLoggingMiddleware)
    register_exception_handlers(app)

    root_router = APIRouter(tags=["Operational"])

    @root_router.get(
        "/",
        response_model=RootResponse,
        summary="Welcome",
        description="Returns a welcome message confirming the API is reachable.",
    )
    def read_root() -> RootResponse:
        return RootResponse(message="Welcome to OSSmith API")

    app.include_router(root_router)
    app.include_router(api_router, prefix=settings.API_V1_PREFIX)

    return app


app = create_app()
