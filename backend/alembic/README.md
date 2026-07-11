# alembic/

Database migration environment, managed by [Alembic](https://alembic.sqlalchemy.org/).

- `env.py` — wires Alembic to the application's `Settings.DATABASE_URL` and `Base.metadata`, so migrations never drift from application configuration.
- `script.py.mako` — template used to generate new migration files.
- `versions/` — individual migration scripts. Empty as of Sprint 2, since no models exist yet.

## Usage

```bash
# Generate a new migration after adding/changing a model
alembic revision --autogenerate -m "add thing table"

# Apply all pending migrations
alembic upgrade head

# Roll back the most recent migration
alembic downgrade -1
```

Run these commands from `backend/`, with the same environment (and `.env`) the application itself uses.
