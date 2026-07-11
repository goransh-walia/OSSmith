"""Business logic layer: services.

All business rules live here — never in `api/` route handlers and
never in `repositories/`. Routes call services; services call
repositories. This keeps routes thin, testable, and free of logic
that would otherwise be duplicated across endpoints.

Empty as of Sprint 2 ("Core Platform"). Business logic is explicitly
out of scope for this sprint — see `ROADMAP.md`.
"""
