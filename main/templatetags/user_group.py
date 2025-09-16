# -*- coding: utf-8 -*-
"""
Custom template filters for checking user group membership and superuser status.
"""

from typing import Union

from django import template
from django.contrib.auth.models import User, AnonymousUser

register = template.Library()


@register.filter(name="has_group")
def has_group(user: Union[User, AnonymousUser, None], groups: str) -> bool:
    """
    Check if the given user belongs to at least one of the specified groups.

    Args:
        user: A Django User or AnonymousUser instance.
        groups: A comma-separated string of group names.

    Returns:
        True if user belongs to at least one group, False otherwise.
    """
    if not user or not hasattr(user, "groups"):
        return False

    groups_list = [g.strip().lower() for g in groups.split(",") if g.strip()]
    if not groups_list:
        return False

    return user.groups.filter(name__iexact__in=groups_list).exists()


@register.filter(name="has_group_or_superuser")
def has_group_or_superuser(user: Union[User, AnonymousUser, None], groups: str) -> bool:
    """
    Check if the given user is either a superuser or belongs to at least one of the specified groups.

    Args:
        user: A Django User or AnonymousUser instance.
        groups: A comma-separated string of group names.

    Returns:
        True if user is superuser or in one of the groups, False otherwise.
    """
    if not user or not hasattr(user, "is_superuser"):
        return False
    if user.is_superuser:
        return True
    return has_group(user, groups)
