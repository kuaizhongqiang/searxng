# SPDX-License-Identifier: AGPL-3.0-or-later
"""Stub: external bang redirect — removed for JSON API-only mode."""

import typing as t

from searx.data import EXTERNAL_BANGS  # noqa: F401 — re-export for engines

__all__ = ['get_bang_url', 'get_bang_definition_and_autocomplete', 'resolve_bang_definition']


def get_bang_url(search_query: t.Any, external_bangs_db: dict | None = None) -> str | None:
    return None


def get_bang_definition_and_autocomplete(
    bang: str, external_bangs_db: dict | None = None
) -> tuple[str | None, list[str]]:
    return (None, [])


def get_bang_definition_and_ac(external_bangs_db: dict, bang: str) -> tuple | None:
    return None


def get_node(external_bangs_db: dict, bang: str) -> dict | None:
    return None


def resolve_bang_definition(bang_definition: str, query: str) -> tuple[str, int]:
    return (query, 0)

