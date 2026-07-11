"""API layer: route definitions.

Routes are intentionally "thin" — they validate input via
`app/schemas/`, delegate to `app/services/`, and translate the result
into an HTTP response. Business logic never lives here.
"""
