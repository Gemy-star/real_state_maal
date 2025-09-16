# -*- coding: utf-8 -*-
"""
Template tag to expose the application version.
Reads from a RELEASE file in the project root.
"""

import os
from functools import lru_cache

from django import template
from django.conf import settings

register = template.Library()


@lru_cache(maxsize=1)
def _read_version() -> str:
    """
    Read version string from RELEASE file, if available.
    Falls back to settings.VERSION or 'dev' if not found.
    """
    release_path = os.path.join(settings.BASE_DIR, "RELEASE")

    try:
        with open(release_path, encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return getattr(settings, "VERSION", "dev")
    except Exception as e:
        # Log if needed
        return f"unknown ({e.__class__.__name__})"


@register.simple_tag(name="get_version")
def get_version() -> str:
    """
    Django template tag to return the current application version.

    Usage in templates:
        {% load version_tags %}
        Version: {% get_version %}
    """
    return _read_version()
