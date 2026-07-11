"""Pydantic schemas defining request and response shapes.

Schemas are the API's public contract and are kept separate from
`app/models/` (SQLAlchemy ORM classes), which represent persistence,
not the wire format. A schema may map closely to a model, but the two
are never the same class.
"""
