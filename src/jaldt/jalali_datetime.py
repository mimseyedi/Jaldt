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


class JalaliIntegerMonth(int, Enum):
    now = 0
    farvardin = 1
    ordibehesht = 2
    khordad = 3
    tir = 4
    mordad = 5
    shahrivar = 6
    mehr = 7
    aban = 8
    azar = 9
    dey = 10
    bahman = 11
    esfand = 12


def g2j(gy: int, gm: int, gd: int) -> List[int]:
    """
    Convert Gregorian date to Jalali.
    The function to convert the Gregorian date to Jalali is taken from the following link:
    https://jdf.scr.ir/jdf/python

    :param gy: Gregorian year: int
    :param gm: Gregorian month: int
    :param gd: Gregorian day: int
    :return: List[jalali_year: int, jalali_month: int, jalali_day: int]
    """

    for arg in [gy, gm, gd]:
        if not isinstance(arg, int):
            raise TypeError('All arguments must be int. No other type is acceptable.')

    g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

    if (gm > 2):
        gy2 = gy + 1
    else:
        gy2 = gy

    days = 355666 + (365 * gy) + ((gy2 + 3) // 4) - ((gy2 + 99) // 100) + ((gy2 + 399) // 400) + gd + g_d_m[gm - 1]
    jy = -1595 + (33 * (days // 12053))
    days %= 12053
    jy += 4 * (days // 1461)
    days %= 1461

    if (days > 365):
        jy += (days - 1) // 365
        days = (days - 1) % 365

    if (days < 186):
        jm = 1 + (days // 31)
        jd = 1 + (days % 31)
    else:
        jm = 7 + ((days - 186) // 30)
        jd = 1 + ((days - 186) % 30)

    return [jy, jm, jd]


def j2g(jy: int, jm: int, jd: int) -> List[int]:
    """
    Convert Jalali date to Gregorian.
    The function to convert the Jalali date to Gregorian is taken from the following link:
    https://jdf.scr.ir/jdf/python

    :param jy: Jalali year: int
    :param jm: Jalali month: int
    :param jd: Jalali day: int
    :return: List[[gregorian_year: int, gregorian_month: int, gregorian_day: int]]
    """

    for arg in [jy, jm, jd]:
        if not isinstance(arg, int):
            raise TypeError('All arguments must be int. No other type is acceptable.')

    jy += 1595
    days = -355668 + (365 * jy) + ((jy // 33) * 8) + (((jy % 33) + 3) // 4) + jd

    if (jm < 7):
        days += (jm - 1) * 31
    else:
        days += ((jm - 7) * 30) + 186

    gy = 400 * (days // 146097)
    days %= 146097
    if (days > 36524):
        days -= 1
        gy += 100 * (days // 36524)
        days %= 36524
        if (days >= 365):
            days += 1

    gy += 4 * (days // 1461)
    days %= 1461
    if (days > 365):
        gy += ((days - 1) // 365)
        days = (days - 1) % 365
    gd = days + 1

    if ((gy % 4 == 0 and gy % 100 != 0) or (gy % 400 == 0)):
        kab = 29
    else:
        kab = 28
    sal_a = [0, 31, kab, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    gm = 0

    while (gm < 13 and gd > sal_a[gm]):
        gd -= sal_a[gm]
        gm += 1

    return [gy, gm, gd]

