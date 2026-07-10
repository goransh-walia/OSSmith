# Architecture

This document describes the technical architecture of OSSmith: how the system is structured, why it's structured that way, and what constraints future contributors should respect.

It will grow alongside the codebase. As of Sprint 1, it describes the intended shape of the system; implementation lands in subsequent pull requests.

## 1. System Overview

OSSmith is a monorepo containing two independently deployable applications connected by a versioned HTTP API:

```
┌─────────────────────┐        HTTP / JSON        ┌──────────────────────┐
│                      │ ─────────────────────────▶│                      │
│   frontend/          │                            │   backend/           │
│   Next.js 15 (React) │◀───────────────────────────│   FastAPI (Python)   │
│                      │                            │                      │
└─────────────────────┘                            └──────────────────────┘
```

- **Frontend** — a Next.js application responsible for everything the user sees and interacts with.
- **Backend** — a FastAPI application responsible for business logic, data access, and (in later sprints) orchestration of AI mentoring workflows.

The two communicate exclusively over a documented HTTP API. Neither imports the other's code directly. This boundary is intentional: it keeps each application independently testable, deployable, and understandable by a contributor who only wants to work on one side.

## 2. Why This Stack

| Choice | Rationale |
|---|---|
| Next.js 15 / React 19 | Mature ecosystem, strong TypeScript support, excellent contributor familiarity — lowers the barrier for new contributors, which matters for a project about *becoming* a contributor. |
| FastAPI | Async-first, Pydantic-native validation, automatic OpenAPI docs — the generated API docs double as living documentation for contributors exploring the backend. |
| Pydantic v2 | Strict, explicit data contracts between layers; catches schema issues at development time rather than runtime. |
| uv | Fast, reproducible Python dependency management with lockfile guarantees. |
| SQLAlchemy + Alembic | Industry-standard ORM and migration tooling; installed in Sprint 1 so future schema work has a consistent foundation, but not wired into business logic yet. |
| Tailwind CSS + shadcn/ui | Utility-first styling with accessible, composable component primitives — fast to extend without fighting a heavy design system. |
| Docker / Docker Compose | Consistent local development environment regardless of contributor OS; a first-time contributor should be able to run `docker compose up` and have a working environment. |

## 3. Repository Structure

```
OSSmith/
├── .github/                   # Community health files, issue/PR templates, CI workflows
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── backend/                    # FastAPI application (added in PR #2)
│   ├── app/
│   │   ├── api/                # Route definitions, versioned
│   │   ├── core/                # App-wide concerns: logging, error handling, startup
│   │   ├── config/              # Settings / environment configuration
│   │   ├── schemas/             # Pydantic request/response models
│   │   ├── models/               # SQLAlchemy ORM models
│   │   ├── services/             # Business logic, orchestration
│   │   └── utils/                # Small, pure helper functions
│   ├── tests/
│   └── main.py
├── frontend/                   # Next.js application (added in PR #3)
│   ├── app/                     # App Router routes
│   ├── components/              # Reusable UI components
│   ├── hooks/                   # Custom React hooks
│   ├── lib/                     # Client utilities, API client
│   ├── styles/                  # Global styles / Tailwind config
│   └── public/                  # Static assets served as-is
├── docs/                        # Extended documentation beyond the root-level docs
├── assets/                      # Shared static assets (logos, diagrams) used across docs/apps
├── scripts/                     # Developer tooling and automation scripts
├── docker/                      # Dockerfiles and compose configuration
├── README.md
├── ROADMAP.md
├── ARCHITECTURE.md
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── LICENSE
├── .env.example
├── docker-compose.yml
├── .gitignore
├── .editorconfig
└── .pre-commit-config.yaml
```

Every top-level folder is expected to carry its own `README.md` once it contains code, explaining its purpose and conventions to a contributor opening it for the first time.

## 4. Backend Design Principles

These principles govern backend work starting in PR #2 and are documented here so contributors can plan ahead:

- **Layered architecture.** Routes (`api/`) stay thin; they validate input via `schemas/` and delegate to `services/`. Business logic never lives in route handlers.
- **Dependency injection.** FastAPI's dependency system is used for things like settings, database sessions, and (later) authentication — never global mutable state.
- **Explicit configuration.** All configuration flows through a single `Settings` class backed by environment variables, never scattered `os.environ` calls.
- **Typed everywhere.** Full type hints, checked with `mypy`. Pydantic v2 models define every request and response shape.
- **Errors are structured.** API errors return a consistent, documented shape rather than raw stack traces or ad hoc dictionaries.

## 5. Frontend Design Principles

- **App Router, server-first.** Favor React Server Components; reach for client components only when interactivity requires it.
- **Composable UI.** Build on shadcn/ui primitives rather than one-off custom components, so the design system stays coherent as the app grows.
- **No premature state management.** Local and server state first; a global store is only introduced when a concrete need arises.
- **Accessibility is not optional.** Semantic HTML, keyboard navigability, and color contrast are reviewed as part of every UI pull request.

## 6. Data Flow (Target State)

Once the AI mentor exists (Sprint 4+), the intended flow is:

1. User action in the frontend triggers a request to a versioned backend endpoint.
2. The backend validates the request, applies business logic in `services/`, and — where AI assistance is involved — orchestrates a human-in-the-loop mentoring interaction rather than an autonomous action.
3. Any code changes, commits, or pull requests are always presented to the user for review and explicit action. The backend never pushes to GitHub on the user's behalf without that explicit step.

This flow directly encodes Product Principle #3: **the human always stays in control.**

## 7. Testing Strategy

| Layer | Tooling | Scope |
|---|---|---|
| Backend unit/integration | `pytest` | Services, schemas, API routes |
| Frontend unit | `Vitest` | Components, hooks, utilities |
| Frontend end-to-end | `Playwright` | Critical user flows |

CI (added in a later Sprint 1 PR) runs lint, type-check, and test suites for both applications on every pull request.

## 8. Non-Goals for Sprint 1

To keep scope honest, the following are explicitly **not** part of the architecture yet, and any pull request introducing them during Sprint 1 should be redirected to a later sprint:

- Authentication / authorization
- GitHub API integration
- Database logic beyond startup wiring
- Issue recommendation logic
- Any AI agent or LLM integration
- Business/domain logic of any kind

## 9. Open Questions

This section will track architecture decisions still under discussion. Contributors are encouraged to raise proposals as GitHub Discussions or issues rather than resolving them silently inside unrelated PRs.

- Final approach to AI orchestration (direct API calls vs. an agent framework) — to be decided ahead of Sprint 4.
- Multi-tenancy / user isolation strategy — to be decided ahead of Sprint 2.
