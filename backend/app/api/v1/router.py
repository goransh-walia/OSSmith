"""Aggregates all v1 routers into a single router mounted by `app.main`."""

from fastapi import APIRouter

from app.api.v1 import health, version

api_router = APIRouter()
api_router.include_router(health.router)
api_router.include_router(version.router)
