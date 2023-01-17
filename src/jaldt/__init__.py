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


# Version.
__version__ = "1.0.0"

# Version tuple
VERSION = tuple(__version__.split('.'))


__all__ = ["g2j",
           "j2g",
           "now",
           "calendar",
           "events",
           "__version__",
           "VERSION",]


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


def calendar(month: JalaliStringMonth='now', lang: Language='farsi',
             color: CalendarColor='def', style: CalendarStyle='highlight') -> None:
    """
    Jalali calendar is printed by this function.

    :param month: Jalali month in lower string format
    :param lang: Jalali calendar language ('farsi', 'fingilish')
    :param color: Jalali calendar color
    :param style: Current day display style
    :return: None
    """

    if month not in set(JalaliStringMonth):
        raise TypeError(f'Only {[jalali_month.value for jalali_month in JalaliStringMonth]} are allowed')

    if lang not in set(Language):
        raise TypeError(f'Only {[language.value for language in Language]} are allowed.')

    if color not in set(CalendarColor):
        raise TypeError(f'Only {[calcolor.value for calcolor in CalendarColor]} are allowed.')

    if style not in set(CalendarStyle):
        raise TypeError(f'Only {[calstyle.value for calstyle in CalendarStyle]} are allowed.')


    ansi_colors = {"def": "\033[0m", "gray": "\033[90m", "red": "\033[91m",
                   "blue": '\x1b[94m', "green": "\033[92m", "yellow": "\033[93m",
                   "pink": "\033[95m", 'cyan': '\x1b[36m', 'black': '\x1b[30m'}

    ansi_styles = {"highlight": "\033[100m", "underline": "\033[4m", "blink": "\033[5m"}

    jalali_months = ['farvardin', 'ordibehesht', 'khordad',
                     'tir', 'mordad', 'shahrivar',
                     'mehr', 'aban', 'azar',
                     'dey', 'bahman', 'esfand']

    jalali_months_farsi = ['فروردین', 'اردیبهشت', 'خرداد',
                           'تیر', 'مرداد', 'شهریور',
                           'مهر', 'آبان', 'آذر',
                           'دی', 'بهمن', 'اسفند']

    farsi_numbers = {'0': ' ۰', '1': ' ۱', '2': ' ۲', '3': ' ۳', '4': ' ۴',
                     '5': ' ۵', '6': ' ۶', '7': ' ۷', '8': ' ۸', '9': ' ۹',
                     '10': '۱۰', '11': '۱۱', '12': '۱۲', '13': '۱۳', '14': '۱۴',
                     '15': '۱۵', '16': '۱۶', '17': '۱۷', '18': '۱۸', '19': '۱۹',
                     '20': '۲۰', '21': '۲۱', '22': '۲۲', '23': '۲۳', '24': '۲۴',
                     '25': '۲۵', '26': '۲۶', '27': '۲۷', '28': '۲۸', '29': '۲۹',
                     '30': '۳۰', '31': '۳۱'}

    jalali_days_farsi = ['۲ش', '۳ش', '۴ش', '۵ش', 'جم', 'شن', '۱ش']
    days_after_current_day_farsi = {'۲ش': 5, '۳ش': 4, '۴ش': 3, '۵ش': 2, 'جم': 1, 'شن': 7, '۱ش': 6}

    jalali_days = ['2s', '3s', '4s', '5s', 'jo', 'sh', '1s']
    days_after_current_day = {'2s': 5, '3s': 4, '4s': 3, '5s': 2, 'jo': 1, 'sh': 7, '1s': 6}

    days_space_to_print_first_day = {'2s': 14, '3s': 11, '4s': 8, '5s': 5, 'jo': 2, 'sh': 20, '1s': 17}

    g_year, g_month, g_day = datetime.now().year, datetime.now().month, datetime.now().day
    j_year, j_month, j_day = g2j(g_year, g_month, g_day)

    is_leap_year = lambda jalali_year: True if (jalali_year - 1399) % 4 == 0 else False

    current_year = j_year

    if month == 'now':
        current_month = jalali_months[j_month - 1]
        first_day_of_month_in_g = j2g(j_year, j_month, 1)
    else:
        current_month = month
        first_day_of_month_in_g = j2g(current_year, jalali_months.index(month) + 1, 1)

    month_days = 31 if current_month in jalali_months[:6] else (
        30 if current_month in jalali_months[6:11] else (30 if is_leap_year(current_year) else 29))

    current_date = 1

    if lang == 'farsi':
        farsi_year = ''.join([farsi_numbers[number] for number in str(current_year)]).replace(" ", '')
        month_title = f'{ansi_colors[color]}{farsi_year} {jalali_months_farsi[jalali_months.index(current_month)]}'
        month_title_space = ((20 // 2) + len(month_title) // 2) - len(month_title) + 3

        j_weekday = jalali_days_farsi[datetime(first_day_of_month_in_g[0],
                                               first_day_of_month_in_g[1],
                                               first_day_of_month_in_g[2]).weekday()]

        first_day_to_print = days_after_current_day_farsi[j_weekday]
        last_line_space = {0: 18, 1: 5, 2: 8, 3: 11, 4: 14, 5: 17, 6: 20}

        print(" " * month_title_space + month_title)
        for _ in range(20):
            print("—", end='')

        print('\n' + 'شن ۱ش ۲ش ۳ش ۴ش ۵ش جم')

        for i in range(first_day_to_print, current_date - 1, -1):
            print(f'{farsi_numbers[str(i)]}', end=' ')
            current_date += 1
        print()

        while current_date <= month_days:
            c = 6
            if current_date + 6 > month_days:
                c = c - ((current_date + 6) - month_days)
            for i in range(current_date + c, current_date - 1, -1):
                if current_date > month_days:
                    break
                if i == month_days:
                    if i != current_date:
                        space = 20 - last_line_space[i - current_date]
                        if i == j_day and jalali_months.index(current_month) + 1 == j_month:
                            print(f"{ansi_styles[style]}{farsi_numbers[str(i)]}\033[0m", end=' ')
                        else:
                            print(" " * space + f"{ansi_colors[color]}{farsi_numbers[str(i)]}", end=' ')
                    else:
                        if i == j_day and jalali_months.index(current_month) + 1 == j_month:
                            print(f"{ansi_styles[style]}{farsi_numbers[str(i)]}\033[0m", end=' ')
                        else:
                            print(" " * 18 + f"{ansi_colors[color]}{farsi_numbers[str(i)]}", end=' ')
                else:
                    if i == j_day and jalali_months.index(current_month) + 1 == j_month:
                        print(f"{ansi_styles[style]}{farsi_numbers[str(i)]}\033[0m", end=' ')
                    else:
                        print(f"{ansi_colors[color]}{farsi_numbers[str(i)]}", end=' ')
                current_date += 1
            print("\033[0m")

    else:
        month_title = f'{ansi_colors[color]}{current_month.capitalize()} {current_year}'
        month_title_space = ((20 // 2) + len(month_title) // 2) - len(month_title) + 3

        j_weekday = jalali_days[datetime(first_day_of_month_in_g[0],
                                         first_day_of_month_in_g[1],
                                         first_day_of_month_in_g[2]).weekday()]

        space_to_print_first_day = 20 - days_space_to_print_first_day[j_weekday]

        print(" " * month_title_space + month_title)
        for _ in range(20):
            print("—", end='')

        print('\n' + 'sh 1s 2s 3s 4s 5s jo')

        print(" " * space_to_print_first_day, end='')

        for date in range(current_date, days_after_current_day[j_weekday] + 1):
            print(f' {current_date}', end=' ')
            current_date += 1
        print()

        while current_date <= month_days:
            for _ in range(7):
                if current_date > month_days:
                    break
                if current_date < 10:
                    if current_date == j_day and jalali_months.index(current_month) + 1 == j_month:
                        print(f" {ansi_styles[style]}{current_date}\033[0m", end=' ')
                    else:
                        print(f" {ansi_colors[color]}{current_date}", end=' ')
                else:
                    if current_date == j_day and jalali_months.index(current_month) + 1 == j_month:
                        print(f"{ansi_styles[style]}{current_date}\033[0m", end=' ')
                    else:
                        print(f"{ansi_colors[color]}{current_date}", end=' ')
                current_date += 1
            print("\033[0m")


def events(month: Union[JalaliStringMonth, JalaliIntegerMonth]='now', inplace: bool=False) -> Dict[str, str]:
    """
    The events of the month are printed or returned by this function.

    :param month: Jalali month in string or integer format
    :param inplace: Have a return value or not? (True: inplace, False: return)
    :return: None or Dict[str, str]
    """

    if not isinstance(inplace, bool):
        raise TypeError('Only bool is acceptable.')

    if month not in set(JalaliStringMonth) and month not in set(JalaliIntegerMonth):
        raise TypeError(f'Only {[jalali_month.value for jalali_month in JalaliStringMonth]} or ' +
                         f'{[jalali_month.value for jalali_month in JalaliIntegerMonth]} are allowed.')


    events_of_months = {'farvardin': {'۱': 'جشن نوروز/جشن سال نو',
                                      '۲': 'عید نوروز',
                                      '۳': ['روز جهانی هواشناسی', 'عید نوروز'],
                                      '۴': 'عیدنوروز',
                                      '۶': [' زادروز آشو زرتشت، اَبَراِنسان بزرگ تاریخ', 'روز امید، روز شادباش نویسی'],
                                      '۷': 'روز جهانی تئاتر',
                                      '۱۰': 'جشن آبانگاه',
                                      '۱۲': 'روز جمهوری اسلامی',
                                      '۱۳': 'جشن سیزده به در',
                                      '۱۷': 'سروش روز ،جشن سروشگان',
                                      '۱۸': 'روز جهانی بهداشت',
                                      '۱۹': 'روز جشن فروردینگان',
                                      '۲۳': 'روز دندانپزشک',
                                      '۲۵': 'روز بزرگداشت عطار نیشابوری',
                                      '۲۹': 'روز ارتش جمهوری اسلامی ایران',
                                      '۳۰': 'روز علوم آزمایشگاهی، زاد روز حکیم سید اسماعیل جرجانی'},

                        'ordibehesht': {'۱': 'روز بزرگداشت سعدی',
                                        '۲': 'جشن گیاه آوری؛ روز زمین',
                                        '۳': 'روزبزرگداشت شیخ بهایی؛ روزملی کارآفرینی؛ روز معماری',
                                        '۷': 'روز جهانی طراحی و گرافیک',
                                        '۹': ['روز ملی روانشناس و مشاور', 'روزشوراها'],
                                        '۱۰': 'جشن چهلم نوروز؛ روز ملی خلیج فارس',
                                        '۱۱': 'روزجهانی کارگر',
                                        '۱۲': 'روز معلم',
                                        '۱۵': ['روز جهانی ماما', 'جشن میانه بهار/جشن بهاربد؛ روز شیراز'],
                                        '۱۸': 'روز جهانی صلیب سرخ و هلال احمر',
                                        '۲۲': 'زادروز مریم میرزاخانی ریاضیدان ایرانی، روز جهانی زن در ریاضیات',
                                        '۲۵': 'روز بزرگداشت فردوسی',
                                        '۲۷': 'روز ارتباطات و روابط عمومی',
                                        '۲۸': ['روز جهانی موزه و میراث فرهنگی', 'روز بزرگداشت حکیم عمر خیام']},

                        'khordad': {'۱': ['روز بزرگداشت ملاصدرا', 'روز بهره وری و بهینه سازی مصرف'],
                                    '۳': 'فتح خرمشهر در عملیات بیت المقدس و روز مقاومت، ایثار و پیروزی',
                                    '۴': 'روز دزفول، روز مقاومت و پایداری',
                                    '۶': 'خرداد روز،جشن خردادگان',
                                    '۱۰': 'روز جهانی بدون دخانیات',
                                    '۱۴': 'رحلت حضرت امام خمینی',
                                    '۱۵': ['روز جهانی محیط زیست', 'قیام ۱۵ خرداد'],
                                    '۲۰': 'روز جهانی صنایع دستی',
                                    '۲۲': 'روز جهانی مبارزه با کار کودکان',
                                    '۲۴': 'رروز جهانی اهدای خون',
                                    '۲۵': 'روز ملی گل وگیاه',
                                    '۲۷': ['روز جهانی بیابان زدایی', 'روز جهاد کشاورزی']},

                        'tir': {'۱': ['روز اصناف', 'جشن آب پاشونک، جشن آغاز تابستان'],
                                '۵': 'روز جهانی مبارزه با مواد مخدر',
                                '۷': 'انفجار دفتر حزب جمهوری اسلامی و شهادت دکتر بهشتی و ۷۲ نفر از اعضای حزب؛ روز قوه قضاییه',
                                '۸': 'روز مبارزه با سلاح های شیمیایی و میکروبی',
                                '۱۰': 'روز صنعت و معدن',
                                '۱۲': 'شلیک به پرواز ۶۵۵ ایران ایر توسط ناو وینسنس',
                                '۱۳': 'تیر روز،جشن تیرگان',
                                '۱۴': 'روز قلم',
                                '۱۵': 'جشن خام خواری',
                                '۲۲': 'زادروز محمد خوارزمی، ریاضیدان و فیلسوف ایرانی و روز ملی فناوری اطلاعات',
                                '۲۵': 'روز بهزیستی و تامین اجتماعی',
                                '۲۷': ' اعلام پذیرش قطعنامه ۵۹۸ شورای امنیت از سوی ایران'},

                        'mordad': {'۶': 'روز ترویج آموزش های فنی و حرفه ای',
                                   '۷': 'َمرداد روز، جشن اَمردادگان',
                                   '۸': 'روز بزرگداشت شیخ شهاب الدین سهروردی',
                                   '۱۰': ['آغاز هفته جهانی شیردهی', 'جشن چله تابستان'],
                                   '۱۴': 'صدور فرمان مشروطیت',
                                   '۱۷': 'روز خبرنگار',
                                   '۲۲': 'روز جهانی چپ دست ها',
                                   '۲۸': [' روز جهانی عکاسی',
                                          'سالروز فاجعه آتش زدن سینما رکس آبادان',
                                          'سالروز وقایع ۲۸ مرداد پس از برکناری محمد مصدق']},

                        'shahrivar': {'۱': 'روز بزرگداشت ابوعلی سینا و روز پزشک',
                                      '۲': ' آغاز هفته دولت',
                                      '۴': ['شهریور روز، جشن شهریورگان', ' زادروز داراب (کوروش)'],
                                      '۵': 'روز بزرگداشت محمدبن زکریای رازی و روز داروساز',
                                      '۸': 'انفجار در دفتر نخست‌وزیری جمهوری اسلامی ایران، روز مبارزه با تروریسم',
                                      '۱۱': 'روز صنعت چاپ',
                                      '۱۳': 'روز بزرگداشت ابوریحان بیرونی',
                                      '۱۷': 'قیام ۱۷ شهریور',
                                      '۱۹': 'روز جهانی پیشگیری از خودکشی',
                                      '۲۰': 'حمله به برج‌های دوقلوی مرکز تجارت جهانی',
                                      '۲۱': 'روز سینما',
                                      '۲۲': ['به قتل رسیدن مهسا امینی توسط جمهوری اسلامی در سال ۱۴۰۱ و شروع اعتراضات سراسری (زن، زندگی، آزادی)',
                                             'روز گرامیداشت برنامه نویسان'],
                                      '۲۷': 'روز شعر و ادب پارسی و روز بزرگداشت استاد شهریار',
                                      '۳۰': 'روز جهانی صلح',
                                      '۳۱': 'آغاز هفته دفاع مقدس'},

                        'mehr': {'۱': 'آغاز حمله مغول به ایران در پاییز ۵۹۸ خورشیدی',
                                 '۵': 'روز جهانی جهانگردی',
                                 '۷': [' سقوط هواپیمای حامل جمعی از فرماندهان جنگ (کلاهدوز، نامجو، فلاحی، فکوری، جهان آرا) در سال ۱۳۶۰',
                                     'روز آتش نشانی و ایمنی',
                                     'روز بزرگداشت شمس تبریزی'],
                                 '۸': ['جمعه خونین زاهدان، اعتراضات سراسری سال ۱۴۰۱',
                                     'روز جهانی ترجمه و مترجم',
                                     'روز جهانی ناشنوایان',
                                     'روز بزرگداشت مولوی'],
                                 '۹': 'روز جهانی سالمندان',
                                 '۱۰': 'مهر روز،جشن مهرگان',
                                 '۱۲': 'آغاز هفته جهانی فضا',
                                 '۱۳': ['روز جهانی معلم', 'روز نیروی انتظامی'],
                                 '۱۴': 'روز دامپزشکی',
                                 '۱۶': 'روز ملی کودک',
                                 '۱۷': 'روز جهانی پست',
                                 '۱۸': 'روز جهانی مبارزه با حکم اعدام',
                                 '۱۹': 'روز جهانی دختر',
                                 '۲۰': 'روز بزرگداشت حافظ',
                                 '۲۱': 'روز پیروزی کاوه و فریدون بر ضحاک',
                                 '۲۲': 'روز جهانی استاندارد',
                                 '۲۳': 'روز جهانی عصای سفید',
                                 '۲۴': 'روز جهانی غذا',
                                 '۲۵': 'روز جهانی ریشه کنی فقر',
                                 '۲۶': 'روز تربیت بدنی و ورزش',
                                 '۲۹': 'روز ملی کوهنورد'},

                        'aban': {'۱': 'روز آمار و برنامه ریزی',
                                 '۷': 'سالروز ورود کوروش بزرگ به بابل در سال ۵۳۹ پیش از میلاد',
                                 '۸': 'روز نوجوان',
                                 '۱۰': 'آبان روز، جشن آبانگان',
                                 '۱۳': 'روز دانش آموز',
                                 '۱۴': 'روز فرهنگ عمومی',
                                 '۱۵': 'جشن میانه پاییز',
                                 '۱۸': 'روز ملی کیفیت',
                                 '۲۳': 'روز جهانی دیابت',
                                 '۲۴': ['شروع اعتراضات سراسری به دلیل گران شدن نرخ بنزین در سال ۱۳۹۸', 'روز کتاب و کتابخوانی'],
                                 '۲۶': 'روز جهانی فلسفه',
                                 '۲۸': 'روز جهانی آقایان',
                                 '۲۹': 'روز جهانی کودک'},

                        'azar': {'۱': 'آذر جشن',
                                 '۴': 'روز جهانی مبارزه با خشونت علیه زنان',
                                 '۵': 'روز بسیج مستضعفان',
                                 '۷': 'روز نیروی دریایی',
                                 '۹': 'جشن آذرگان ،آذر روز',
                                 '۱۰': ['روز جهانی ایدز', 'روز مجلس'],
                                 '۱۲': 'روز جهانی معلولان',
                                 '۱۳': 'روز بیمه',
                                 '۱۵': 'روز حسابدار',
                                 '۱۶': 'روز دانشجو',
                                 '۱۹': 'روز جهانی حقوق بشر',
                                 '۲۰': 'روز جهانی کوه نوردی',
                                 '۲۵': 'روز پژوهش',
                                 '۲۶': 'روز حمل و نقل',
                                 '۳۰': 'جشن شب یلدا'},

                        'dey': {'۱': 'روز میلاد خورشید؛ جشن خرم روز، نخستین جشن دیگان',
                                '۴': ['روز بزرگداشت دوستی', 'جشن کریسمس'],
                                '۵': ['سالروز شهادت آشو زرتشت، اَبَراِنسان بزرگ تاریخ', 'زمین لرزه ی بم ۱۳۸۲'],
                                '۸': 'دی به آذر روز، دومین جشن دیگان',
                                '۱۱': 'جشن آغاز سال نو میلادی',
                                '۱۳': 'شهادت سردار حاج قاسم سلیمانی در سال ۱۳۹۸',
                                '۱۵': 'دی به مهر روز، سومین جشن دیگان',
                                '۱۶': 'غرق شدن کشتی سانچی در سال ۱۳۹۶',
                                '۱۸': 'شلیک به پرواز ۷۵۲ هواپیمایی اوکراین توسط جمهوری اسلامی در سال ۱۳۹۸',
                                '۱۹': 'درگذشت اکبر هاشمی رفسنجانی در سال ۱۳۹۵',
                                '۲۰': 'قتل امیرکبیر به دستور ناصرالدین شاه قاجار در سال ۱۲۳۰',
                                '۲۳': 'دی به دین روز، چهارمین جشن دیگان',
                                '۳۰': 'آتش سوزی و فروریختن ساختمان پلاسکو در سال ۱۳۹۵'},

                        'bahman': {'۱': 'زادروز فردوسی',
                                   '۲': 'بهمن روز، جشن بهمنگان',
                                   '۵': 'جشن نوسره',
                                   '۱۰': 'جشن سده',
                                   '۱۲': 'بازگشت امام خمینی به ایران',
                                   '۱۵': 'جشن میانه زمستان',
                                   '۱۹': 'روز نیروی هوایی',
                                   '۲۲': ['حمله به سفارت روسیه و قتل گریبایدوف سفیر روسیه تزاری در ایران', 'پیروزی انقلاب اسلامی'],
                                   '۲۳': 'زادروز چارلز داروین بنیانگذار نظریه‌ی فرگشت از طریق انتخاب طبیعی',
                                   '۲۵': 'جشن ولنتاین',
                                   '۲۹': ['فاجعه انفجار قطار نیشابور در سال ۱۳۸۲', 'جشن سپندارمذگان و روز عشق']},

                        'esfand': {'۵': ['روز بزرگداشت خواجه نصیر الدین طوسی و روز مهندس', 'روز بزرگداشت زمین و بانوان'],
                                   '۷': ['سالروز درگذشت علی اکبر دهخدا', 'سالروز استقلال کانون وکلای دادگستری و روز وکیل مدافع'],
                                   '۱۵': 'روز درختکاری',
                                   '۱۸': 'روزجهانی زنان',
                                   '۲۴': 'روز جهانی عدد پی',
                                   '۲۵': 'پایان سرایش شاهنامه',
                                   '۲۹': 'روز ملی شدن صنعت نفت ایران'}}


    jalali_integer_months = {1: 'farvardin', 2: 'ordibehesht', 3: 'khordad',
                             4: 'tir', 5: 'mordad', 6: 'shahrivar',
                             7: 'mehr', 8: 'aban', 9: 'azar',
                             10: 'dey', 11: 'bahman', 12: 'esfand'}

    jalali_farsi_months = {'farvardin': 'فروردین', 'ordibehesht': 'اردیبهشت', 'khordad': 'خرداد',
                           'tir': 'تیر', 'mordad': 'مرداد', 'shahrivar': 'شهریور',
                           'mehr': 'مهر', 'aban': 'آبان', 'azar': 'آذر',
                           'dey': 'دی', 'bahman': 'بهمن', 'esfand': 'اسفند'}

    if inplace:
        if isinstance(month, int):
            month_title = now(strftime='%B', lang='farsi') if month == 0 else jalali_farsi_months[jalali_integer_months[month]]

            if month != 0:
                for day, event in events_of_months[jalali_integer_months[month]].items():
                    print(f'{month_title} {day}: {" - ".join(event) if isinstance(event, list) else event}')
            else:
                current_month = now(strftime='%B', lang='fingilish')
                for day, event in events_of_months[current_month].items():
                    print(f'{month_title} {day}: {" - ".join(event) if isinstance(event, list) else event}')
        else:
            month_title = now(strftime='%B', lang='farsi') if month == 'now' else jalali_farsi_months[month]

            if month != 'now':
                for day, event in events_of_months[month].items():
                    print(f'{month_title} {day}: {" - ".join(event) if isinstance(event, list) else event}')
            else:
                current_month = now(strftime='%B', lang='fingilish')
                for day, event in events_of_months[current_month].items():
                    print(f'{month_title} {day}: {" - ".join(event) if isinstance(event, list) else event}')

    else:
        if isinstance(month, int):
            return events_of_months[jalali_integer_months[month]] if month != 0 else events_of_months[now(strftime='%B', lang='fingilish')]

        return events_of_months[month] if month != 'now' else events_of_months[now(strftime='%B', lang='fingilish')]
