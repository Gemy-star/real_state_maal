# -*- coding: utf-8 -*-

import os

from django import template
from django.conf import settings

register = template.Library()

_version = None


@register.simple_tag
def get_version() -> str:
    """Return application version defined in RELEASE file"""
    global _version
    if not _version:
        with open(os.path.join(settings.BASE_DIR, "RELEASE"), encoding="utf-8") as f:
            _version = f.read()

    return _version
