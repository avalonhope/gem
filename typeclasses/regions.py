"""
Region
Regions are simple containers located within a Country.
"""

from evennia import DefaultRoom


class Region(DefaultRoom):
    """
    Regions are like any Object, except their location is within a Country. They also use basetype_setup() to
    add locks so they cannot be puppeted or picked up.
    (to change that, use at_object_creation instead)
    See examples/object.py for a list of
    properties and methods available on all Objects.
    """

    pass