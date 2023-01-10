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


def now(strftime: StrfTimeFormat='default', lang: Language='farsi') -> str:
    """
    Returns the current date and time in Jalali.

    :param strftime: The strftime format for the return value
    :param lang: The language of the return value ('farsi', 'fingilish')
    :return: str
    """

    if lang not in set(Language):
        raise TypeError(f'Only {[language.value for language in Language]} are allowed.')

    farsi_numbers = {'0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
                     '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'}

    farsi_weekday = {'Monday': 'دوشنبه', 'Tuesday': 'سه شنبه', 'Wednesday': 'چهارشنبه',
                     'Thursday': 'پنجشنبه', 'Friday': 'جمعه', 'Saturday': 'شنبه', 'Sunday': 'یکشنبه'}

    fingilish_weekday = {'Monday': '2shanbe', 'Tuesday': '3shanbe', 'Wednesday': '4shanbe',
                         'Thursday': '5shanbe', 'Friday': 'jomeh', 'Saturday': 'shanbe', 'Sunday': '1shanbe'}

    jalali_farsi_months = {1: 'فروردین', 2: 'اردیبهشت', 3: 'خرداد',
                           4: 'تیر', 5: 'مرداد', 6: 'شهریور',
                           7: 'مهر', 8: 'آبان', 9: 'آذر',
                           10: 'دی', 11: 'بهمن', 12: 'اسفند'}

    jalali_fingilish_months = {1: 'farvardin', 2: 'ordibehesht', 3: 'khordad',
                               4: 'tir', 5: 'mordad', 6: 'shahrivar',
                               7: 'mehr', 8: 'aban', 9: 'azar',
                               10: 'dey', 11: 'bahman', 12: 'esfand'}

    current_datetime = datetime.now()

    jalali_date = g2j(current_datetime.year,
                      current_datetime.month,
                      current_datetime.day)

    def convert_numbers(string_of_numbers: str) -> str:
        string_with_farsi_numbers = ''
        for char in string_of_numbers:
            if char.isdigit():
                string_with_farsi_numbers += farsi_numbers[char]
            else:
                string_with_farsi_numbers += char

        return string_with_farsi_numbers


    add_zero = lambda number: f'0{str(number)}' if number < 10 else str(number)

    if strftime == 'default':
        jalali_date = '/'.join(list(map(str, g2j(current_datetime.year,
                                                 current_datetime.month,
                                                 current_datetime.day))))
        if lang == 'farsi':
            return convert_numbers(jalali_date) + ' ' + convert_numbers(str(current_datetime.time()))
        else:
            return jalali_date + ' ' + str(current_datetime.time())

    else:
        output, index = '', 0

        while index < len(strftime):
            if strftime[index] == '%' and index != len(strftime) - 1:

                if strftime[index + 1] != '-':
                    symbol = strftime[index] + strftime[index + 1]
                else:
                    symbol = f'{strftime[index]}{strftime[index + 1]}{strftime[index + 2]}'

                if symbol in set(StrfTimeFormat):
                    if symbol == '%a':
                        weekday = current_datetime.strftime('%A')
                        output += farsi_weekday[weekday][:3] if lang == 'farsi' else fingilish_weekday[weekday][:3]

                    elif symbol == '%A':
                        weekday = current_datetime.strftime('%A')
                        output += farsi_weekday[weekday] if lang == 'farsi' else fingilish_weekday[weekday]

                    elif symbol == '%-d':
                        output += convert_numbers(str(jalali_date[2])) if lang == 'farsi' else str(jalali_date[2])

                    elif symbol == '%d':
                        output += convert_numbers(add_zero(jalali_date[2])) if lang == 'farsi' else add_zero(jalali_date[2])

                    elif symbol == '%b':
                        output += jalali_farsi_months[jalali_date[1]][:3] if lang == 'farsi' else jalali_fingilish_months[jalali_date[1]][:3]

                    elif symbol == '%B':
                        output += jalali_farsi_months[jalali_date[1]] if lang == 'farsi' else jalali_fingilish_months[jalali_date[1]]

                    elif symbol == '%-m':
                        output += convert_numbers(str(jalali_date[1])) if lang == 'farsi' else str(jalali_date[1])

                    elif symbol == '%m':
                        output += convert_numbers(add_zero(jalali_date[1])) if lang == 'farsi' else add_zero(jalali_date[1])

                    elif symbol == '%Y':
                        output += convert_numbers(str(jalali_date[0])) if lang == 'farsi' else str(jalali_date[0])

                    elif symbol == '%y':
                        output += convert_numbers(str(jalali_date[0]))[-2:] if lang == 'farsi' else str(jalali_date[0])[-2:]

                    elif symbol == '%-H':
                        output += convert_numbers(str(current_datetime.strftime('%-H'))) if lang == 'farsi' else \
                            str(current_datetime.strftime('%-H'))

                    elif symbol == '%H':
                        output += convert_numbers(
                            str(current_datetime.strftime('%H'))) if lang == 'farsi' else \
                            str(current_datetime.strftime('%H'))

                    elif symbol == '%-I':
                        output += convert_numbers(str(current_datetime.strftime('%-I'))) if lang == 'farsi' else \
                            str(current_datetime.strftime('%-I'))

                    elif symbol == '%I':
                        output += convert_numbers(
                            str(current_datetime.strftime('%I'))) if lang == 'farsi' else str(current_datetime.strftime('%I'))

                    elif symbol == '%p':
                        am_or_pm = str(current_datetime.strftime('%p'))
                        if lang == 'farsi':
                            output += 'صبح' if am_or_pm == 'AM' else 'بعد از ظهر'
                        else:
                            output += am_or_pm

                    elif symbol == '%-M':
                        output += convert_numbers(str(current_datetime.strftime('%-M'))) if lang == 'farsi' else str(
                            current_datetime.strftime('%-M'))

                    elif symbol == '%M':
                        output += convert_numbers(str(current_datetime.strftime('%M'))) if lang == 'farsi' else str(
                            current_datetime.strftime('%M'))

                    elif symbol == '%-S':
                        output += convert_numbers(str(current_datetime.strftime('%-S'))) if lang == 'farsi' else str(
                            current_datetime.strftime('%-S'))

                    elif symbol == '%S':
                        output += convert_numbers(str(current_datetime.strftime('%S'))) if lang == 'farsi' else str(
                            current_datetime.strftime('%S'))

                else:
                    raise TypeError(f'Only {[strf.value for strf in StrfTimeFormat]} are allowed.')

                index += 2 if len(symbol) == 2 else 3
            else:
                output += strftime[index]
                index += 1

        return output