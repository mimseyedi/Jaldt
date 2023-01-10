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


class StrfTimeFormat(str, Enum):
    default = 'default'
    short_weekday_name = "%a"
    full_weekday_name = "%A"
    day_of_month = '%-d'
    day_of_month_with_zero = '%d'
    short_month_name = '%b'
    full_month_name = '%B'
    month = '%-m'
    month_with_zero = '%m'
    year = '%Y'
    year_without_century_with_zero = '%y'
    hour_24 = '%-H'
    hour_24_with_zero = '%H'
    hour_12 = '%-I'
    hour_12_with_zero = '%I'
    am_or_pm = '%p'
    minute = '%-M'
    minute_with_zero = '%M'
    second = '%-S'
    second_with_zero = '%S'


class Language(str, Enum):
    farsi = 'farsi'
    fingilish = 'fingilish'


class CalendarStyle(str, Enum):
    highlight = 'highlight'
    underline = 'underline'
    blink = 'blink'


class CalendarColor(str, Enum):
    default = 'def'
    black = 'black'
    red = 'red'
    blue = 'blue'
    cyan = 'cyan'
    green = 'green'
    yellow = 'yellow'
    pink = 'pink'
    gray = 'gray'


class JalaliStringMonth(str, Enum):
    now = 'now'
    farvardin = 'farvardin'
    ordibehesht = 'ordibehesht'
    khordad = 'khordad'
    tir = 'tir'
    mordad = 'mordad'
    shahrivar = 'shahrivar'
    mehr = 'mehr'
    aban = 'aban'
    azar = 'azar'
    dey = 'dey'
    bahman = 'bahman'
    esfand = 'esfand'