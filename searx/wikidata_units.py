# SPDX-License-Identifier: AGPL-3.0-or-later
"""Stub: wikidata unit conversion — removed for JSON API-only mode."""

__all__ = ['convert_from_si', 'convert_to_si', 'symbol_to_si']

import typing as t


def convert_from_si(si_name: str, symbol: str, value: float | int) -> float:
    return float(value)


def convert_to_si(si_name: str, symbol: str, value: float | int) -> float:
    return float(value)


def units_by_si_name(si_name: str) -> dict:
    return {}


def symbol_to_si() -> dict[str, tuple[str, int]]:
    return {}


def fetch_units():
    pass
