# SPDX-License-Identifier: AGPL-3.0-or-later
"""Lightweight babel.core replacement for SearXNG-core."""

from __future__ import annotations

from . import UnknownLocaleError  # noqa: F401

# Minimal territory → languages mapping for SearXNG engine use.
# Extracted from CLDR common-data. Only covers countries that
# SearXNG engines commonly query.
_TERRITORY_LANGUAGES: dict[str, dict[str, float]] = {
    # Major English-speaking
    "US": {"en": 1},
    "GB": {"en": 1},
    "AU": {"en": 1},
    "CA": {"en": 1, "fr": 0.3},
    "NZ": {"en": 1},
    "IE": {"en": 1, "ga": 0.1},
    # Chinese
    "CN": {"zh": 1},
    "TW": {"zh": 1},
    "HK": {"zh": 1, "en": 0.5},
    "SG": {"en": 1, "zh": 0.5, "ms": 0.3, "ta": 0.2},
    # Japan / Korea
    "JP": {"ja": 1},
    "KR": {"ko": 1},
    # Europe
    "DE": {"de": 1},
    "FR": {"fr": 1},
    "IT": {"it": 1},
    "ES": {"es": 1},
    "PT": {"pt": 1},
    "NL": {"nl": 1},
    "BE": {"nl": 0.6, "fr": 0.4, "de": 0.1},
    "CH": {"de": 0.7, "fr": 0.2, "it": 0.1, "rm": 0.01},
    "AT": {"de": 1},
    "SE": {"sv": 1},
    "NO": {"nb": 1, "nn": 0.1},
    "DK": {"da": 1},
    "FI": {"fi": 1, "sv": 0.1},
    "PL": {"pl": 1},
    "RU": {"ru": 1},
    "CZ": {"cs": 1},
    "SK": {"sk": 1},
    "HU": {"hu": 1},
    "RO": {"ro": 1},
    "BG": {"bg": 1},
    "GR": {"el": 1},
    "UA": {"uk": 1},
    "TR": {"tr": 1},
    # South America
    "BR": {"pt": 1},
    "AR": {"es": 1},
    "MX": {"es": 1},
    "CL": {"es": 1},
    "CO": {"es": 1},
    # Middle East / South Asia
    "IN": {"hi": 0.4, "en": 0.3, "bn": 0.1, "te": 0.1, "mr": 0.1, "ta": 0.1, "ur": 0.1, "gu": 0.1, "kn": 0.1, "ml": 0.1, "or": 0.1, "pa": 0.1},
    "PK": {"ur": 1, "en": 0.5},
    "BD": {"bn": 1},
    "ID": {"id": 1},
    "MY": {"ms": 1, "en": 0.3, "zh": 0.2, "ta": 0.1},
    "PH": {"en": 1, "fil": 0.5},
    "TH": {"th": 1},
    "VN": {"vi": 1},
    "SA": {"ar": 1},
    "AE": {"ar": 1, "en": 0.3},
    "IL": {"he": 1, "ar": 0.2, "en": 0.3},
    "EG": {"ar": 1},
    # Africa
    "ZA": {"en": 1, "af": 0.1, "zu": 0.1, "xh": 0.1},
    "NG": {"en": 1, "ha": 0.3, "yo": 0.2, "ig": 0.2},
}


def get_global(key: str) -> dict[str, dict[str, float]]:
    """Return CLDR global data (stub)."""
    if key == "territory_languages":
        return _TERRITORY_LANGUAGES
    raise KeyError(f"Unknown CLDR global key: {key}")
