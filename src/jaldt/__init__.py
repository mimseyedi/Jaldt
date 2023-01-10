"""
jaldt

Author: Mohammad Seyedi
Description: Jaldt is a package for working with date and time based on Jalali calendar and date.

jaldt is open source under the MIT license and you can easily use it
and make any changes you like and share it with others.

Github repo: https://github.com/mimseyedi/Jaldt
"""


from jalali_datetime import g2j, j2g, now, calendar, events

# Version variable.
__version__ = "1.0.0"

# Version tuple
VERSION = tuple(__version__.split('.'))


__all__ = [
    # Functions.
    "g2j",
    "j2g",
    "now",
    "calendar",
    "events",
    # Version info.
    "__version__",
    "VERSION",
]
