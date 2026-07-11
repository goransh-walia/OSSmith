# =========================================================
# OSSmith Backend — Dockerfile
# =========================================================
# Multi-stage build:
#   1. `builder` installs dependencies into a virtual environment
#      using uv, so the runtime image never needs a compiler toolchain.
#   2. `runtime` copies only the venv and application code, runs as a
#      non-root user, and starts uvicorn.
# =========================================================

# ---------- builder ----------
FROM python:3.12-slim AS builder

# Install uv (fast, reproducible Python package management)
COPY --from=ghcr.io/astral-sh/uv:0.5.4 /uv /uvx /usr/local/bin/

WORKDIR /build

# Copy dependency metadata and source together — hatchling needs the
# `app/` package present to build the project for installation.
COPY pyproject.toml ./
COPY app ./app

RUN uv venv /opt/venv \
    && uv pip install --python /opt/venv/bin/python .

# ---------- runtime ----------
FROM python:3.12-slim AS runtime

# Create a non-root user to run the application.
RUN groupadd --gid 1000 ossmith \
    && useradd --uid 1000 --gid ossmith --shell /bin/bash --create-home ossmith

ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY --from=builder /opt/venv /opt/venv

WORKDIR /app
COPY --chown=ossmith:ossmith . .

USER ossmith

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
