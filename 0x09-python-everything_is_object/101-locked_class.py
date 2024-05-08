#!/usr/bin/python3
"""Define a 'LockedClass'."""


class LockedClass:
    """
    This LockedClass prevent user from creating a new
    instance attributes except if the the new instance
    attribute is called 'first_name'.
    """
    __slots__ = ["first_name"]
