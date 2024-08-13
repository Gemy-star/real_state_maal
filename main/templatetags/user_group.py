# -*- coding: utf-8 -*-

from django import template
from django.contrib.auth.models import User


register = template.Library()


@register.filter
def has_group(user: User, groups: str) -> bool:
    """Return True if given user is member of at least one of the given groups names (comma separated)"""
    groups_list = [group.strip() for group in groups.split(",")]
    return user.groups.filter(name__in=groups_list).exists()


@register.filter
def has_group_or_superuser(user: User, groups: str) -> bool:
    """Return True if given user is member of at least one of the given groups names (comma separated) or is a superuser"""
    return user.is_superuser or has_group(user, groups)
