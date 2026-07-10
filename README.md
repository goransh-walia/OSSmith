<div align="center">

# OSSmith

**Craft your Open Source Journey.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Code of Conduct](https://img.shields.io/badge/Code%20of%20Conduct-active-blueviolet.svg)](CODE_OF_CONDUCT.md)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](#)
[![Frontend](https://img.shields.io/badge/frontend-Next.js%2015-000000.svg)](#tech-stack)
[![Backend](https://img.shields.io/badge/backend-FastAPI-009688.svg)](#tech-stack)

[Getting Started](#getting-started) •
[Documentation](#documentation) •
[Roadmap](ROADMAP.md) •
[Contributing](CONTRIBUTING.md)

</div>

---

## Mission

OSSmith is an AI-powered mentor that teaches developers how to become great open-source contributors.

Unlike bots that automate pull requests, OSSmith does **not** exist to submit code on your behalf. It exists to **teach**. OSSmith helps you:

- Discover repositories that match your skills and interests
- Understand unfamiliar codebases and their architecture
- Read and interpret issues the way a maintainer would
- Learn Git and GitHub workflows properly, not just by copy-pasting commands
- Implement fixes with guidance, not automation
- Run and understand tests
- Prepare high-quality, maintainer-friendly pull requests
- Learn from code review feedback instead of dreading it

**The human always stays in control. The AI never blindly submits code.**

## Why OSSmith Exists

Most tools built around open source either automate contributions away from the human (bots, auto-PR generators) or leave newcomers to figure everything out alone. Both approaches fail the people open source needs most: developers who want to learn how to contribute well.

OSSmith sits in between — an AI mentor that explains the "why" behind every step, so the skills transfer to the next repository, the next issue, and the next contributor you help in turn.

## Product Principles

| # | Principle |
|---|-----------|
| 1 | Teach before solving |
| 2 | Understand before coding |
| 3 | Human stays in control |
| 4 | Quality over quantity |
| 5 | Respect maintainers |
| 6 | Build contributors instead of bots |
| 7 | Every interaction should help the user learn |

## Features

> OSSmith is under active development. Sprint 1 establishes the project foundation; feature work begins in subsequent sprints. See [ROADMAP.md](ROADMAP.md) for the full plan.

- 🔍 **Repository Discovery** — find projects aligned with your skills and interests *(planned)*
- 🧭 **Codebase Onboarding** — guided architecture walkthroughs for unfamiliar repos *(planned)*
- 🧩 **Issue Comprehension** — understand what a maintainer is actually asking for *(planned)*
- 🎓 **Git & GitHub Coaching** — learn the workflow, not just the commands *(planned)*
- ✅ **Test-Driven Guidance** — understand and run a project's test suite *(planned)*
- 📝 **PR Preparation** — write pull requests maintainers want to review *(planned)*
- 💬 **Review Literacy** — learn how to read and respond to code review *(planned)*

## Screenshots

> _Screenshots will be added as the UI is built out in upcoming sprints._

| Landing Page | Dashboard | Issue Explorer |
|:---:|:---:|:---:|
| _coming soon_ | _coming soon_ | _coming soon_ |

## Tech Stack

**Frontend**
Next.js 15 · React 19 · TypeScript · Tailwind CSS · shadcn/ui · ESLint · Prettier

**Backend**
Python 3.12+ · FastAPI · Pydantic v2 · uv · SQLAlchemy · Alembic

**Testing**
pytest (backend) · Vitest & Playwright (frontend)

**Code Quality**
Black · Ruff · mypy · pre-commit

**Infrastructure**
Docker · Docker Compose · GitHub Actions

See [ARCHITECTURE.md](ARCHITECTURE.md) for the full technical rationale.

## Architecture

OSSmith is a monorepo composed of an independently deployable frontend and backend, connected by a versioned API contract. For diagrams and detailed design decisions, see [ARCHITECTURE.md](ARCHITECTURE.md).

```
OSSmith/
├── backend/     # FastAPI application
├── frontend/    # Next.js application
├── docs/        # Project documentation
├── assets/      # Shared static assets (logos, diagrams)
├── scripts/     # Developer tooling and automation scripts
├── docker/      # Container definitions
└── .github/     # Issue templates, PR template, workflows
```

## Getting Started

> **Note:** Sprint 1 establishes repository structure and documentation only. Application code (backend/frontend) lands in subsequent pull requests. The steps below reflect the intended workflow once that code is merged.

### Prerequisites

- [Git](https://git-scm.com/) 2.40+
- [Node.js](https://nodejs.org/) 20+ and a package manager (npm, pnpm, or yarn)
- [Python](https://www.python.org/) 3.12+
- [uv](https://github.com/astral-sh/uv) for Python dependency management
- [Docker](https://www.docker.com/) and Docker Compose (optional, for containerized development)

### Installation

```bash
# Clone the repository
git clone https://github.com/<org>/OSSmith.git
cd OSSmith

# Copy environment variables
cp .env.example .env

# Backend setup (once backend code is added)
cd backend
uv sync
uv run uvicorn app.main:app --reload

# Frontend setup (once frontend code is added, in a new terminal)
cd frontend
npm install
npm run dev
```

### Running with Docker

```bash
docker compose up --build
```

## Documentation

| Document | Description |
|---|---|
| [ROADMAP.md](ROADMAP.md) | Where the project is headed, sprint by sprint |
| [ARCHITECTURE.md](ARCHITECTURE.md) | System design, folder structure, and technical decisions |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute code, docs, or ideas |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Community standards |
| [SECURITY.md](SECURITY.md) | How to report vulnerabilities |

## Roadmap

OSSmith is being built sprint by sprint, in the open. Sprint 1 focuses purely on the professional foundation — no AI, no auth, no business logic. See the full [ROADMAP.md](ROADMAP.md) for what's next.

## Contributing

OSSmith is an open-source project about learning to do open source well — so we hold contributions to that same standard. Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request, and note that this repository is governed by our [Code of Conduct](CODE_OF_CONDUCT.md).

Good first steps:

1. Read [ARCHITECTURE.md](ARCHITECTURE.md) to understand how the project fits together.
2. Check open issues labeled [`good first issue`](https://github.com/<org>/OSSmith/issues).
3. Comment on the issue before starting work, so effort isn't duplicated.

## FAQ

**Is OSSmith a bot that opens pull requests for me?**
No. OSSmith explains, guides, and reviews — you write and submit the code, with a full understanding of what it does and why.

**Does OSSmith work with any GitHub repository?**
That capability is planned but not yet implemented. See [ROADMAP.md](ROADMAP.md) for status.

**Is OSSmith free and open source?**
Yes. OSSmith is released under the [MIT License](LICENSE).

**How can I help?**
Read [CONTRIBUTING.md](CONTRIBUTING.md) — and if you're new to open source, using OSSmith to contribute to OSSmith itself is a great place to start.

## License

OSSmith is released under the [MIT License](LICENSE).

---

<div align="center">

Built to turn developers into open-source contributors — one well-understood pull request at a time.

</div>
