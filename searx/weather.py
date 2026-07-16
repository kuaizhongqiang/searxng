# SPDX-License-Identifier: AGPL-3.0-or-later
"""Stub: weather module — removed for JSON API-only mode."""

from __future__ import annotations

import typing as t
import datetime

WeatherConditionType: t.TypeAlias = str


class Temperature:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class Pressure:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class WindSpeed:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class RelativeHumidity:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class Compass:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


class DateTime:
    time: datetime.datetime
    timezone: str

    def __init__(self, time: datetime.datetime | None = None, timezone: str = 'UTC'):
        self.time = time or datetime.datetime.now(datetime.timezone.utc)
        self.timezone = timezone

    def __str__(self) -> str:
        return str(self.time)

    def l10n(self, locale: str, format: str = 'medium') -> str:
        return str(self.time)

    def l10n_date(self, locale: str, format: str = 'medium') -> str:
        return str(self.time.date())


class GeoLocation:
    name: str
    latitude: float
    longitude: float
    timezone: str
    country: str
    country_code: str

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def by_query(cls, search_term: str) -> GeoLocation | None:
        return None


def symbol_url(condition: str) -> str | None:
    return None
