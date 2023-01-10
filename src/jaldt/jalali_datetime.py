"""
jaldt

Author: Mohammad Seyedi
Description: Jaldt is a package for working with date and time based on Jalali calendar and date.

jaldt is open source under the MIT license and you can easily use it
and make any changes you like and share it with others.

Github repo: https://github.com/mimseyedi/Jaldt
"""


from datetime import datetime
from typing import List, Union, Dict
from enum import Enum


__all__ = [
    "g2j",
    "j2g",
    "now",
    "calendar",
    "events",
]

