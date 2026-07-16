# SPDX-License-Identifier: AGPL-3.0-or-later
"""Lightweight babel.languages replacement for SearXNG-core."""

from __future__ import annotations

from .core import _TERRITORY_LANGUAGES


def get_official_languages(territory: str, regional: bool = True, de_facto: bool = True) -> set[str]:
    """Return set of official language codes for a territory.

    Mimics babel.languages.get_official_languages().
    """
    langs = _TERRITORY_LANGUAGES.get(territory.upper(), {})
    return set(langs.keys())
