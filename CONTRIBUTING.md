# Contributing to OSSmith

First off — thank you. OSSmith exists to help developers become great open-source contributors, so we try to hold this repository to the standard we teach. Using OSSmith's own contribution process is one of the best ways to learn it.

This guide covers how to propose changes, our expectations for code and documentation, and how pull requests get reviewed and merged.

## Before You Start

1. Read [README.md](README.md) to understand the mission and product principles.
2. Read [ARCHITECTURE.md](ARCHITECTURE.md) to understand how the project is structured.
3. Read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — it applies to every interaction in this repository.
4. Check the [ROADMAP.md](ROADMAP.md) to see what's currently in scope. Pull requests that introduce out-of-scope work for the current sprint will be asked to wait.

## Ways to Contribute

You don't need to write code to contribute meaningfully:

- **Report bugs** using the [Bug Report](/.github/ISSUE_TEMPLATE/bug_report.md) template.
- **Propose features** using the [Feature Request](/.github/ISSUE_TEMPLATE/feature_request.md) template — please explain how the idea supports our product principles.
- **Improve documentation** — clarity fixes, typo fixes, and better examples are always welcome.
- **Answer questions** on open issues from other contributors, especially newcomers.
- **Review pull requests** — thoughtful review is as valuable as code.

## Finding Something to Work On

- Look for issues labeled `good first issue` if you're new to the project.
- Look for issues labeled `help wanted` for higher-impact work.
- **Comment on the issue before starting work.** This avoids duplicated effort and gives maintainers a chance to flag context you might not have.
- If no issue exists for what you want to do, open one first. Pull requests without a linked issue may be asked to open one, except for trivial fixes (typos, broken links).

## Development Setup

> Sprint 1 currently contains repository structure and documentation only. Once backend and frontend code land (PR #2 and #3), this section will include full local setup steps. In the meantime:

```bash
git clone https://github.com/<org>/OSSmith.git
cd OSSmith
cp .env.example .env
```

Refer to [README.md](README.md#getting-started) for the latest setup instructions as they become available.

## Branching and Commits

- Branch from `main` using a descriptive name: `feature/short-description`, `fix/short-description`, `docs/short-description`.
- Write commit messages in the imperative mood: `Add health check endpoint`, not `Added` or `Adds`.
- Keep commits focused. A commit should represent one logical change.
- We loosely follow [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`, `chore:`, `test:`, `refactor:`) — not strictly enforced yet, but appreciated.

## Code Standards

These apply once application code exists; documented here so contributors know what to expect.

**Backend (Python)**
- Format with `black`, lint with `ruff`, type-check with `mypy`.
- Full type hints on all functions and methods.
- Business logic lives in `services/`, not in route handlers.
- No commented-out code, no `TODO`s left in merged code — open an issue instead.

**Frontend (TypeScript)**
- Format with `prettier`, lint with `eslint`.
- No `any` types without a documented reason.
- Components should be small and composable; prefer composition over configuration props.

**All contributions**
- No dead code, no placeholder/fake implementations, no duplicated logic.
- Public functions, endpoints, and components should be documented well enough that a first-time reader understands their purpose without asking the author.

## Testing

- New backend logic should include `pytest` coverage.
- New frontend components/hooks should include `Vitest` coverage; user-facing flows may warrant a `Playwright` test.
- Pull requests that reduce test coverage without a documented reason will be asked to add tests before merge.

## Pull Request Process

1. Fork the repository (or create a branch, if you have write access) and make your changes.
2. Ensure lint, type-check, and test suites pass locally.
3. Fill out the [pull request template](/.github/PULL_REQUEST_TEMPLATE.md) completely — incomplete templates slow down review.
4. Link the issue your PR addresses.
5. Keep the PR scoped to that issue. Unrelated changes should be a separate PR.
6. A maintainer will review your PR. Expect questions — they're part of the learning process this project is built around, not a sign something is wrong.
7. Once approved and CI passes, a maintainer will merge your PR.

## Code Review Philosophy

Reviews on OSSmith are meant to teach, not gatekeep. As a contributor, you can expect reviewers to:

- Explain *why* a change is requested, not just *what* to change.
- Distinguish between "this must change before merge" and "consider this for the future."
- Respond within a reasonable timeframe — if you haven't heard back in a week, a polite ping is welcome.

As a reviewer (once you're in a position to review others), please extend the same care, especially to first-time contributors.

## Documentation Contributions

Documentation is treated as a first-class contribution, not a lesser one. If you're improving `README.md`, `ARCHITECTURE.md`, or any doc in `docs/`, the same PR process applies. Clear writing is reviewed with the same rigor as code.

## Questions?

Open an issue using the [Question](/.github/ISSUE_TEMPLATE/question.md) template. There's no such thing as a question too basic — helping people ask questions well is part of what OSSmith is for.

Thank you for contributing to OSSmith, and welcome to the project.
