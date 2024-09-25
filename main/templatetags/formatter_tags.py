# -*- coding: utf-8 -*-

"""
Custom formatter tags and filters
"""

from typing import Any, Optional

from django import template
from django.template.defaultfilters import date

register = template.Library()


@register.filter
def format_date(value) -> str:
    """Format the given datetime object"""
    if getattr(value, "tzinfo", None):
        return date(value, "Y-m-d H:i:s (e)")
    return date(value, "Y-m-d H:i:s")


@register.filter
def startswith(value: str, prefix: str) -> bool:
    """Return True if given value starts with given prefix"""
    return value.startswith(prefix)


@register.filter
def get_key_value(dictionary: dict, key: Any) -> Optional[Any]:
    """
    Custom template filter to get the value of a key from a dictionary.
    """
    return dictionary.get(key, None)
