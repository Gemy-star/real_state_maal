# -*- coding: utf-8 -*-
"""
Custom formatter tags and filters for Django templates.
Provides safe utilities for formatting dates, working with strings, and handling dicts.
"""

from typing import Any, Optional

from django import template
from django.template.defaultfilters import date
from django.utils.formats import date_format
from django.utils.timezone import is_aware

register = template.Library()


@register.filter(name="format_date")
def format_date(value: Any, fmt: str = "Y-m-d H:i:s") -> str:
    """
    Format a datetime object into a human-readable string.
    - Falls back to empty string if value is None or not a date.
    - Supports timezone-aware datetimes.
    - Uses Django’s `date_format` for i18n/l10n.
    """
    if not value:
        return ""
    try:
        if is_aware(value):
            return date(value, f"{fmt} (e)")
        return date(value, fmt)
    except Exception:
        # fallback using Django’s localized formatter
        return date_format(value, fmt) if hasattr(value, "strftime") else str(value)


@register.filter(name="startswith")
def startswith(value: Any, prefix: str) -> bool:
    """
    Return True if the string `value` starts with the given prefix.
    Case-insensitive by default.
    """
    if not isinstance(value, str) or not isinstance(prefix, str):
        return False
    return value.lower().startswith(prefix.lower())


@register.filter(name="get_key_value")
def get_key_value(dictionary: Any, key: Any) -> Optional[Any]:
    """
    Safely get a value by key from a dictionary-like object.
    - Returns None if dictionary is invalid or key not found.
    """
    try:
        return dictionary.get(key, None)
    except AttributeError:
        return None


@register.filter(name="truncate_chars")
def truncate_chars(value: Any, max_length: int = 50) -> str:
    """
    Truncate a string to a maximum number of characters.
    Appends '...' if the string is longer than max_length.
    """
    if not isinstance(value, str):
        value = str(value) if value is not None else ""
    if len(value) <= max_length:
        return value
    return value[: max_length - 3] + "..."
