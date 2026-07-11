"""Health check endpoint.

Used by orchestrators (Docker, Kubernetes, load balancers) to
determine whether the service is ready to receive traffic. Kept
intentionally simple in Sprint 2 — it does not yet check downstream
dependencies (e.g. database connectivity), since none are relied upon
at request time.
"""

from fastapi import APIRouter

from app.schemas.common import HealthResponse

router = APIRouter(tags=["Operational"])


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Health check",
    description="Returns the current health status of the service.",
)
def get_health() -> HealthResponse:
    """Return a simple liveness signal."""
    return HealthResponse(status="healthy")
