# OSSmith Backend

The OSSmith API — built with [FastAPI](https://fastapi.tiangolo.com/), following a clean, layered architecture designed to support the project for years without a rewrite.

> **Status:** Sprint 2 ("Core Platform"). This sprint delivers infrastructure only — configuration, logging, error handling, the database layer, and three operational endpoints. No business logic, authentication, or AI integration exists yet. See [ROADMAP.md](../ROADMAP.md).

## Architecture

The backend follows a clean, layered structure. Each layer has exactly one responsibility, and dependencies only ever point inward:

```
app/
├── main.py            # Application factory & entrypoint
├── api/
│   └── v1/             # Route definitions (thin — no business logic)
│       ├── router.py    # Aggregates all v1 routers
│       ├── dependencies.py
│       ├── health.py
│       └── version.py
├── core/                # Configuration, logging, lifespan, security, errors
│   ├── config.py
│   ├── logging.py
│   ├── lifespan.py
│   ├── security.py
│   └── exceptions.py
├── database/             # Engine, session, declarative base
│   ├── base.py
│   └── session.py
├── repositories/          # Persistence layer (empty — no models yet)
├── services/               # Business logic layer (empty — Sprint 2 is infra-only)
├── schemas/                 # Pydantic request/response models
│   └── common.py
├── models/                   # SQLAlchemy ORM models (empty — no models yet)
└── utils/                     # Small, pure helper functions (empty)
```

**Rule of thumb:** routes call services, services call repositories, repositories talk to the database. Routes and services never touch the database session directly, and `core/` never imports outward. See [ARCHITECTURE.md](../ARCHITECTURE.md) for the full rationale.

## Prerequisites

- [Python](https://www.python.org/) 3.12+
- [uv](https://github.com/astral-sh/uv) for dependency management
- [Docker](https://www.docker.com/) (optional, for containerized runs)

## Installation

```bash
cd backend
cp .env.example .env
uv sync --extra dev
```

`uv sync` creates a `.venv` and installs both runtime and development dependencies (pytest, ruff, black, mypy, pre-commit).

## Running Locally

```bash
uv run uvicorn app.main:app --reload
```

The API is available at `http://localhost:8000`. With `--reload`, changes to `app/` restart the server automatically.

### Available endpoints (Sprint 2)

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | Welcome message, confirms the API is reachable |
| `GET` | `/health` | Liveness check — used by Docker/orchestrators |
| `GET` | `/version` | Returns project name and current version |

## API Documentation

FastAPI generates interactive API docs automatically:

- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)
- **OpenAPI schema (JSON):** [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

## Running with Docker

```bash
cd backend
docker compose up --build
```

This builds the image and starts the API on `http://localhost:8000`, with data persisted in a named Docker volume (`ossmith-data`) so the SQLite database survives container restarts.

To run just the image directly:

```bash
docker build -t ossmith-backend .
docker run -p 8000:8000 ossmith-backend
```

## Configuration

All configuration is environment-variable driven — see [`.env.example`](.env.example) for the full list, and [`app/core/config.py`](app/core/config.py) for defaults and validation.

| Variable | Default | Description |
|---|---|---|
| `PROJECT_NAME` | `OSSmith` | Project name, shown in API metadata |
| `VERSION` | `0.2.0-alpha` | Application version, returned by `/version` |
| `ENVIRONMENT` | `development` | `development` \| `staging` \| `production` \| `test` |
| `DEBUG` | `true` | Enables verbose logging |
| `HOST` | `0.0.0.0` | Bind host for uvicorn |
| `PORT` | `8000` | Bind port for uvicorn |
| `LOG_LEVEL` | `info` | Minimum log level |
| `DATABASE_URL` | `sqlite:///./ossmith.db` | SQLAlchemy database URL |

## Database & Migrations

The database layer (engine, session, declarative base) is fully wired, but no models exist yet — this is intentional for Sprint 2. Once the first model is added:

```bash
alembic revision --autogenerate -m "add thing table"
alembic upgrade head
```

Alembic reads `DATABASE_URL` from the same `Settings` the application uses, so there's only one source of truth for the database connection. See [`alembic/README.md`](alembic/README.md).

## Testing

```bash
uv run pytest
```

This runs the full suite (`/`, `/health`, `/version`, error handling, and OpenAPI availability) with coverage reporting enabled by default (see `[tool.pytest.ini_options]` in `pyproject.toml`).

## Code Quality

```bash
uv run black .          # format
uv run ruff check .     # lint
uv run mypy app         # type-check
```

All three run in CI (`.github/workflows/backend.yml`) on every pull request touching `backend/`.

### Pre-commit hooks

From the repository root:

```bash
pip install pre-commit
pre-commit install
```

This runs formatting, linting, and type-checking automatically before every commit.

## Logging

The application uses [`structlog`](https://www.structlog.org/) for structured logging. In development, logs are rendered as readable, colorized console output; in production (`ENVIRONMENT=production`), logs are rendered as JSON lines suitable for log aggregation.

Every request is logged with method, path, status code, and latency, and is tagged with a `request_id` that's also returned in the `X-Request-ID` response header — useful for correlating logs to a specific request.

## Error Handling

All errors — expected (`404`, validation failures) and unexpected (unhandled exceptions) — are returned in a single, consistent JSON shape:

```json
{
  "error": {
    "code": "not_found",
    "message": "The requested resource was not found.",
    "request_id": "b3b3c3e0-1234-4a5b-8c9d-abcdef012345"
  }
}
```

See [`app/core/exceptions.py`](app/core/exceptions.py) for the full set of handlers.

## What's Explicitly Not Here Yet

Per the Sprint 2 scope, the following are intentionally absent and will be introduced in later sprints:

- Authentication / authorization
- SQLAlchemy models and business data
- GitHub API integration
- AI / LLM integration of any kind
- Background jobs (Celery/Redis)
- Frontend integration

See [ROADMAP.md](../ROADMAP.md) for what's next.
