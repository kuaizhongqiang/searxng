# SPDX-License-Identifier: AGPL-3.0-or-later
"""Lightweight babel replacement for SearXNG-core.

Provides minimal API compatible with python-babel for SearXNG engine use.
Only implements what SearXNG engines actually use (locale parsing, language lookup).
"""

from __future__ import annotations

import typing as t


class UnknownLocaleError(ValueError):
    """Raised when a locale cannot be parsed."""
    pass


class Locale:
    """Minimal babel.Locale replacement."""

    language: str
    territory: str
    script: str | None

    def __init__(self, language: str, territory: str = '', script: str | None = None):
        self.language = language
        self.territory = territory
        self.script = script

    @staticmethod
    def parse(name: str, sep: str = '-') -> Locale:
        """Parse a locale string like 'en-US' or 'zh-Hans-CN'."""
        parts = name.split(sep)
        lang = parts[0]
        terr = ''
        script = None

        # Handle script subtags (e.g., Hans, Hant, Latn)
        rest = parts[1:]
        if rest and rest[0][0].isupper() and len(rest[0]) == 4:
            script = rest[0]
            rest = rest[1:]
        if rest:
            terr = rest[0]

        return Locale(lang, territory=terr, script=script)

    def __str__(self) -> str:
        parts = [self.language]
        if self.script:
            parts.append(self.script)
        if self.territory:
            parts.append(self.territory)
        return '-'.join(parts)

    def get_language_name(self, locale: str | Locale | None = None) -> str:
        """Return the language name (stub)."""
        return self.language

    @property
    def languages(self) -> dict[str, str]:
        """Return language → name mapping (stub)."""
        return {self.language: self.language}


from . import core as core  # noqa: E402
from . import languages as languages  # noqa: E402
