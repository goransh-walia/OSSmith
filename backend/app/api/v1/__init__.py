"""Version 1 of the OSSmith API.

Routes are organized under a `v1` namespace from day one so future,
breaking API changes can be introduced as `v2` without restructuring
the codebase. In Sprint 2, `API_V1_PREFIX` is empty (see
`app.core.config`), so these routes are served unversioned at the
application root; this is expected to change once the API grows
beyond operational endpoints.
"""
