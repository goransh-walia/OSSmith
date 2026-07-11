"""Shared pytest fixtures.

Sets `ENVIRONMENT=test` before the application is imported, so
`Settings.is_testing` is `True` and logging/config behave accordingly
for the duration of the test session.
"""

import os
from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

os.environ.setdefault("ENVIRONMENT", "test")
os.environ.setdefault("DATABASE_URL", "sqlite:///./test_ossmith.db")

from app.main import create_app


@pytest.fixture
def client() -> Iterator[TestClient]:
    """A `TestClient` bound to a freshly constructed app instance."""
    app = create_app()
    with TestClient(app) as test_client:
        yield test_client
