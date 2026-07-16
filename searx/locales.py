# SPDX-License-Identifier: AGPL-3.0-or-later
"""Stub: SearXNG locale data — removed for JSON API-only mode."""

import typing as t

from searx.sxng_locales import sxng_locales

LOCALE_NAMES: dict[str, str] = {
    'en': 'English',
    'en-US': 'English (US)',
    'zh-Hans-CN': '简体中文',
    'ja': '日本語',
    'ko': '한국어',
    'de': 'Deutsch',
    'fr': 'Français',
    'es': 'Español',
}
LOCALE_BEST_MATCH: dict[str, str] = {}
ADDITIONAL_TRANSLATIONS: dict[str, str] = {}
RTL_LOCALES: list[str] = []
server_locales: list[str] = []


def localeselector():
    return None


def get_translations():
    return None


def get_translation_locales() -> list[str]:
    return []


def locales_initialize():
    pass


def match_locale(searxng_locale: str | None, locale_tag_list: list[str], fallback: str | None = None) -> str | None:
    if not locale_tag_list or not searxng_locale:
        return fallback or 'en'
    if searxng_locale in locale_tag_list:
        return searxng_locale
    lang = searxng_locale.split('-')[0]
    for tag in locale_tag_list:
        if tag.startswith(lang):
            return tag
    return fallback or (locale_tag_list[0] if locale_tag_list else None)


def region_tag(locale: t.Any) -> str:
    return str(locale).split('-')[0] if locale else 'en'


def language_tag(locale: t.Any) -> str:
    return str(locale).split('-')[0] if locale else 'en'


def get_locale(locale_tag: str) -> t.Any | None:
    return None


def get_official_locales(
    territory: str,
    regional: bool = True,
    de_facto: bool = True,
) -> set[t.Any]:
    return set()


def get_engine_locale(
    query_locale: str | None,
    engine_locales: dict[str, str] | set[str],
    default_locale: str = '',
) -> str | None:
    if query_locale is None or not engine_locales:
        return None
    if query_locale in engine_locales:
        return query_locale
    lang = query_locale.split('-')[0]
    for key in engine_locales:
        if key.startswith(lang):
            return key
    return default_locale or lang


def build_engine_locales(engine_traits: dict[str, dict]) -> dict[str, str]:
    return {}
