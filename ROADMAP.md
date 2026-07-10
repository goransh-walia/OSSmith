# Roadmap

This roadmap describes the sprint-by-sprint plan for OSSmith. It will evolve as the project grows and as the community weighs in — open an issue or discussion if you'd like to propose a change.

## Guiding Constraint

Every sprint must leave the repository in a state that reflects our [Product Principles](README.md#product-principles). We would rather ship a smaller, well-documented increment than a large, undocumented one.

## Sprint 1 — Professional Foundation

**Goal:** Establish a production-grade monorepo before any product logic exists.

- [x] PR #1 — Repository foundation: folder structure, governance docs, GitHub templates, licensing
- [ ] PR #2 — Backend foundation: FastAPI skeleton, configuration, health/version endpoints
- [ ] PR #3 — Frontend foundation: Next.js landing page (hero, mission, features, roadmap, architecture, contributing, footer)
- [ ] PR #4 — Tooling and CI: lint, test, and build workflows; pre-commit hooks
- [ ] PR #5 — Docker: backend and frontend Dockerfiles, docker-compose

Explicitly **out of scope** for Sprint 1: authentication, GitHub API integration, database logic beyond startup wiring, issue recommendation, agent system, LLM integration, and business logic of any kind.

## Sprint 2 — Core Data Model (Planned)

- Define the core domain entities (users, learning sessions, repositories, issues)
- Database schema and migrations
- Authentication scaffolding (no third-party GitHub OAuth yet)

## Sprint 3 — GitHub Integration (Planned)

- Read-only GitHub API integration
- Repository and issue browsing
- Rate-limit-aware API client design

## Sprint 4 — The Mentor (Planned)

- First AI mentor experience: codebase and issue comprehension
- Guided, human-in-the-loop explanations (no autonomous code generation)

## Sprint 5 — Guided Contribution Workflow (Planned)

- Git/GitHub workflow coaching
- Test running and interpretation guidance
- PR preparation assistant (draft, never submit, without explicit user action)

## Sprint 6 — Review Literacy (Planned)

- Learning from real review feedback
- Contributor progress tracking

## Beyond

Longer-term ideas we're tracking but haven't committed to a sprint:

- Multi-language codebase support
- Maintainer-facing tools for triaging first-time contributor PRs respectfully
- Community leaderboards focused on learning milestones, not contribution counts

## How to Influence This Roadmap

The roadmap is shaped by the community it serves. If you'd like to propose a change:

1. Open a [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md) issue.
2. Explain how the proposal supports our [Product Principles](README.md#product-principles) — proposals that optimize for automation over learning are unlikely to be accepted.
3. Be open to discussion; roadmap changes are made deliberately, not quickly.
