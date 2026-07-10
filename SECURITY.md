# Security Policy

## Our Commitment

The OSSmith maintainers take security seriously, especially given that OSSmith guides developers through real codebases, real repositories, and eventually real GitHub credentials. We appreciate the efforts of security researchers and users who responsibly disclose vulnerabilities.

## Supported Versions

OSSmith is currently in pre-release, active development (Sprint 1). There is no stable release yet, and no long-term support commitments exist for any particular version.

| Version | Supported |
|---|---|
| `main` (pre-release) | ✅ Security fixes applied |
| Tagged releases | Will be documented here once the first release ships |

This table will be updated as soon as OSSmith reaches its first tagged release.

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them using one of the following private channels:

1. **GitHub Private Vulnerability Reporting** (preferred) — use the "Report a vulnerability" option under this repository's Security tab.
2. **Email** — send details to the maintainers at the security contact listed in the repository's GitHub profile / organization page.

Please include as much of the following as you can:

- A description of the vulnerability and its potential impact
- Steps to reproduce, or a proof-of-concept
- The affected version/commit
- Any suggested remediation, if you have one

## What to Expect

- **Acknowledgment:** we aim to acknowledge new reports within **5 business days**.
- **Assessment:** we will investigate and aim to provide an initial assessment within **10 business days** of acknowledgment.
- **Resolution:** timelines for a fix depend on severity and complexity; we will keep you updated throughout.
- **Disclosure:** we practice coordinated disclosure. We will work with you on an appropriate disclosure timeline once a fix is available, and we're happy to credit reporters who wish to be credited.

## Scope

Given the project's current stage, the following are in scope for security reports:

- The application code in `backend/` and `frontend/` (once merged)
- Infrastructure configuration in `docker/` and CI workflows in `.github/workflows/`
- Dependency vulnerabilities introduced by the project's own lockfiles

The following are generally **out of scope**:

- Vulnerabilities in third-party services OSSmith may integrate with (e.g., GitHub itself) — please report those directly to the relevant vendor.
- Issues that require physical access to a user's device.
- Social engineering attacks against maintainers or contributors.

## Security-Sensitive Design Notes

Because OSSmith is designed around Product Principle #3 — **the human always stays in control** — any pull request that would allow autonomous code submission, credential handling without explicit user consent, or silent write access to a user's GitHub account should be treated as a security-relevant change and flagged for maintainer review, regardless of whether it introduces a traditional vulnerability.

## Thank You

Responsible disclosure helps keep OSSmith, and the contributors who trust it, safe. We're grateful for every report, even ones that turn out not to be exploitable.
