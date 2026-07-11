"""Core application concerns: configuration, logging, lifespan, and security.

Nothing in this package should depend on `api/`, `services/`, or
`repositories/`. Core is the innermost layer of the application and is
imported by everything else — it must never import outward.
"""
