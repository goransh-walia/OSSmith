"""Tests for centralized error handling and API documentation exposure."""

from fastapi.testclient import TestClient


def test_unknown_route_returns_consistent_error_shape(client: TestClient) -> None:
    response = client.get("/this-route-does-not-exist")

    assert response.status_code == 404
    body = response.json()
    assert "error" in body
    assert body["error"]["code"] == "http_error"
    assert "request_id" in body["error"]


def test_ossmith_error_handler_is_registered(client: TestClient) -> None:
    from app.core.exceptions import OSSmithError

    assert OSSmithError in client.app.exception_handlers


def test_openapi_schema_is_available(client: TestClient) -> None:
    response = client.get("/openapi.json")

    assert response.status_code == 200
    schema = response.json()
    assert schema["info"]["title"]
    assert "/health" in schema["paths"]
    assert "/version" in schema["paths"]
    assert "/" in schema["paths"]


def test_swagger_docs_are_available(client: TestClient) -> None:
    response = client.get("/docs")

    assert response.status_code == 200
    assert "swagger" in response.text.lower()
