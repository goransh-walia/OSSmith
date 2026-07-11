"""Tests for `GET /version`."""

from fastapi.testclient import TestClient

from app.core.config import get_settings


def test_version_returns_project_and_version(client: TestClient) -> None:
    settings = get_settings()

    response = client.get("/version")

    assert response.status_code == 200
    assert response.json() == {
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION,
    }
