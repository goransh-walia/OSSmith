"""Tests for `GET /`."""

from fastapi.testclient import TestClient


def test_root_returns_welcome_message(client: TestClient) -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to OSSmith API"}


def test_root_response_includes_request_id_header(client: TestClient) -> None:
    response = client.get("/")

    assert "X-Request-ID" in response.headers
