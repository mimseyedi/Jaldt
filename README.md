# Jaldt

[![pypi](https://img.shields.io/pypi/v/jaldt.svg)](https://pypi.org/project/jaldt/) [![license](https://img.shields.io/github/license/mimseyedi/jaldt.svg)](https://github.com/mimseyedi/Jaldt/blob/master/LICENSE)

![img1](https://raw.githubusercontent.com/mimseyedi/Jaldt/master/docs/images/jaldt_poster.png)

`Jaldt` is a package for working with date and time based on Jalali calendar and date.

## Table of Contents: <a class="anchor" id="contents"></a>
* [How to install](#install)
* [Functions](#funcs)
  
  * [Convert Gregorian date to Jalali](#g2j)
  * [Convert Jalali date to Gregorian](#j2g)
  * [Getting the current date and time by the now function](#now)
   
    * [strftime argument](#strftime_arg)
    * [lang argument](#now_lang_arg)
    
  * [Jalali calendar](#calendar)
  
    * [month argument](#cal_month_arg)
    * [lang argument](#cal_lang_arg)
    * [color argument](#cal_color_arg)
    * [style argument](#cal_style_arg)
    
  * [Jalali monthly events](#events)
  
    * [month argument](#events_month_arg)
    * [inplace argument](#events_inplace_arg)
  
* [Contribute](#cont)
* [Resources](#res)


## How to install <a class="anchor" id="install"></a>
You can download and install this package directly from `pypi` repository by `pip` module. (Make sure you are using Python3)

```
python3 -m pip install jaldt  
```

## Functions <a class="anchor" id="funcs"></a>
This package contains some simple functions to work with date and time in the format of Jalali date, which you can follow the explanations of these functions.

## g2j: <a class="anchor" id="g2j"></a>
With this function, you can easily convert the Gregorian date to Jalali date and receive the output in a list that includes the converted year, month and day.

Example:

```python
from jaldt import g2j

year, month, day = g2j(2023, 1, 10)

print(f'{year}/{month}/{day}')
```

output:
```
1401/10/20
```

## j2g: <a class="anchor" id="j2g"></a>
With this function, you can easily convert the Jalali date to Gregorian date and receive the output in a list that includes the converted year, month and day.

Example:

```python
from jaldt import j2g

year, month, day = j2g(1401, 10, 20)

print(f'{year}/{month}/{day}')
```

output:
```
2023/1/10
```

## now: <a class="anchor" id="now"></a>
With this function, you can get the current date and time in Jalali date with various formats.

Example:

```python
from jaldt import now

current_date_and_time_in_jalali = now()
print(current_date_and_time_in_jalali)
```

output:
```
۱۴۰۱/۱۰/۲۰ ۱۶:۲۳:۰۳.۵۶۰۴۲۲
```

### strftime argument: <a class="anchor" id="strftime_arg"></a>
The strftime argument allows you to specify your desired output by specifying symbols.

Symbol | Description | Output |
--- | --- | ---
`%a` | Abbreviated weekday name. | sha, 1sh, .. 
`%A` | Full weekday name. | shanbe, 1shanbe, ...
`%-d` | Day of the month as a decimal number. | 1, 2, ..., 31
`%d` | Day of the month as a zero added decimal. | 01, 02, ..., 31
`%b` | Abbreviated month name. | far, ord, ..., esf
`%B` | Full month name. | farvardin, ordibehesht, ...
`%-m` | Month as a decimal number. | 1, 2, ..., 12
`%m` | Month as a zero added decimal number. | 01, 02, ..., 12
`%Y` | Year with century as a decimal number. | 1401, 1402, ...
`%y` | Year without century as a zero added decimal number. | 01, 02, ...
`%-H` | Hour (24-hour clock) as a decimal number. | 0, 1, ..., 23
`%H` | Hour (24-hour clock) as a zero added decimal number. | 00, 01, ..., 23
`%-I` | Hour (12-hour clock) as a decimal number. | 1, 2, ..., 12
`%I` | Hour (12-hour clock) as a zero added decimal number. | 01, 02, ..., 12
`%p` | Locale’s AM or PM. | AM, PM
`%-M` | Minute as a decimal number. | 0, 1, ..., 59
`%M` | Minute as a zero added decimal number. | 00, 01, ..., 59
`%-S` | Second as a decimal number. | 0, 1, ..., 59
`%S` | Second as a zero added decimal number. | 00, 01, ..., 59

<br />

Example: Print the current time similar to a 12-hour digital clock.
```python
from jaldt import now

farsi_clock = now(strftime='%I:%M %p', lang='farsi')
fingilish_clock = now(strftime='%I:%M %p', lang='fingilish')

print(farsi_clock)
print(fingilish_clock)
```

output:
```
۰۷:۰۷ بعد از ظهر
07:07 PM
```

### lang argument: <a class="anchor" id="now_lang_arg"></a>
The lang argument is used to specify the output language. It is used in two modes: `farsi` and `fingilish`. The default value of this argument is `farsi`.

Example:
```python
from jaldt import now

farsi_datetime = now(lang='farsi')
fingilish_datetime = now(lang='fingilish')

print(farsi_datetime)
print(fingilish_datetime)
```

output:
```
۱۴۰۱/۱۰/۲۱ ۱۹:۲۵:۳۱.۸۶۲۹۱۲
1401/10/21 19:25:31.862958
```

## calendar: <a class="anchor" id="calendar"></a>
With the calendar function, you can print the Jalali calendar with different `colors` in `farsi` and `fingilish` languages.

Example:
```python
from jaldt import calendar

calendar()
```

output:

![img2](https://raw.githubusercontent.com/mimseyedi/Jaldt/master/docs/images/init_calendar.png)

### month argument: <a class="anchor" id="cal_month_arg"></a>
The month argument allows you to print the calendar of the month you want. The value of this argument must be one of the `Jalali months`, and its default value is `'now'`, which refers to the current month.

Jalali months | Confirmed value 
--- |---| 
فروردین| `'farvardin'`   |
اردیبهشت | `'ordibehesht'` |
خرداد | `'khordad'`     |
تیر | `'tir'`         |
مرداد | `'mordad'`      |
شهریور | `'shahrivar'`   |
مهر | `'mehr'`        |
آبان | `'aban'`        |
آذر | `'azar'`        |
دی | `'dey'`         |
بهمن | `'bahman'`      |
اسفند | `'esfand'`      |

<br />

Example:
```python
from jaldt import calendar

autumn_months = ['mehr', 'aban', 'azar']
for month in autumn_months:
    calendar(month=month, color='yellow')
```

output: 

![img3](https://raw.githubusercontent.com/mimseyedi/Jaldt/master/docs/images/autumn_cal.png)

### lang argument: <a class="anchor" id="cal_lang_arg"></a>
The lang argument is used to specify the output language. It is used in two modes: `farsi` and `fingilish`. The default value of this argument is `farsi`.

Example:
```python
from jaldt import calendar

for language in ['farsi', 'fingilish']:
    calendar(lang=language)
```
output:

![img4](https://raw.githubusercontent.com/mimseyedi/Jaldt/master/docs/images/farsi_fingilish_cal.png)

### color argument: <a class="anchor" id="cal_color_arg"></a>
The color argument allows you to change the color of the calendar using `ANSI` codes. Make sure your `shell` supports ANSI codes!

Colors | ANSI Codes | Confirmed value |
--- |---| --- 
default | `\x1b[0m`  | `'def'`
gray | `\x1b[90m` | `'gray'`
red | `\x1b[91m` | `'red'`
green | `\x1b[92m` | `'green'`
yellow | `\x1b[93m` | `'yellow'`
blue | `\x1b[94m` | `'blue'`
pink | `\x1b[95m` | `'pink'`
cyan | `\x1b[36m` | `'cyan'`
black | `\x1b[30m` | `'black'`

<br />
Example:

```python
from jaldt import calendar

calendar(color='yellow')
```
output:

![img5](https://raw.githubusercontent.com/mimseyedi/Jaldt/master/docs/images/yellow_cal.png)


### style argument: <a class="anchor" id="cal_style_arg"></a>
The style argument allows you to specify how to display the `current day` in three modes: `highlight`, `underline` and `blink`. The default value of this argument is `highlight`.

Example:

```python
from jaldt import calendar

calendar(style='blink')
```

output:

![img6](https://raw.githubusercontent.com/mimseyedi/Jaldt/master/docs/images/blink_cal.gif)


## events: <a class="anchor" id="events"></a>
This function returns all the historical events of the selected month in the form of a dictionary or prints it on the screen.

Example:

```python
from jaldt import events

current_month_events = events()

for day, event in current_month_events.items():
    print(day, event)
```

output:

```
۱ روز میلاد خورشید؛ جشن خرم روز، نخستین جشن دیگان
۴ ['روز بزرگداشت دوستی', 'جشن کریسمس']
۵ ['سالروز شهادت آشو زرتشت، اَبَراِنسان بزرگ تاریخ', 'زمین لرزه ی بم ۱۳۸۲']
۸ دی به آذر روز، دومین جشن دیگان
۱۱ جشن آغاز سال نو میلادی
۱۳ شهادت سردار حاج قاسم سلیمانی در سال ۱۳۹۸
۱۵ دی به مهر روز، سومین جشن دیگان
۱۶ غرق شدن کشتی سانچی در سال ۱۳۹۶
۱۸ شلیک به پرواز ۷۵۲ هواپیمایی اوکراین توسط جمهوری اسلامی در سال ۱۳۹۸
۱۹ درگذشت اکبر هاشمی رفسنجانی در سال ۱۳۹۵
۲۰ قتل امیرکبیر به دستور ناصرالدین شاه قاجار در سال ۱۲۳۰
۲۳ دی به دین روز، چهارمین جشن دیگان
۳۰ آتش سوزی و فروریختن ساختمان پلاسکو در سال ۱۳۹۵
```

### month argument: <a class="anchor" id="events_month_arg"></a>
The month argument allows you to access historical events for any month you choose.

Jalali months | Confirmed value 
--- |---| 
فروردین| `'farvardin'`   |
اردیبهشت | `'ordibehesht'` |
خرداد | `'khordad'`     |
تیر | `'tir'`         |
مرداد | `'mordad'`      |
شهریور | `'shahrivar'`   |
مهر | `'mehr'`        |
آبان | `'aban'`        |
آذر | `'azar'`        |
دی | `'dey'`         |
بهمن | `'bahman'`      |
اسفند | `'esfand'`      |

<br />
Example:

```python
from jaldt import events

aban_events = events(month='aban')

for day, event in aban_events.items():
  print(day, event)
```

output:

```
۱ روز آمار و برنامه ریزی
۷ سالروز ورود کوروش بزرگ به بابل در سال ۵۳۹ پیش از میلاد
۸ روز نوجوان
۱۰ آبان روز، جشن آبانگان
۱۳ روز دانش آموز
۱۴ روز فرهنگ عمومی
۱۵ جشن میانه پاییز
۱۸ روز ملی کیفیت
۲۳ روز جهانی دیابت
۲۴ ['شروع اعتراضات سراسری به دلیل گران شدن نرخ بنزین در سال ۱۳۹۸', 'روز کتاب و کتابخوانی']
۲۶ روز جهانی فلسفه
۲۸ روز جهانی آقایان
۲۹ روز جهانی کودک
```

### inplace argument: <a class="anchor" id="events_inplace_arg"></a>
The inplace argument allows you to get the output or have it automatically printed to the screen. (True Value for printing events)

Example:

```python
from jaldt import events

events(month=6, inplace=True)
```

output:

```
شهریور ۱: روز بزرگداشت ابوعلی سینا و روز پزشک
شهریور ۲:  آغاز هفته دولت
شهریور ۴: شهریور روز، جشن شهریورگان -  زادروز داراب (کوروش)
شهریور ۵: روز بزرگداشت محمدبن زکریای رازی و روز داروساز
شهریور ۸: انفجار در دفتر نخست‌وزیری جمهوری اسلامی ایران، روز مبارزه با تروریسم
شهریور ۱۱: روز صنعت چاپ
شهریور ۱۳: روز بزرگداشت ابوریحان بیرونی
شهریور ۱۷: قیام ۱۷ شهریور
شهریور ۱۹: روز جهانی پیشگیری از خودکشی
شهریور ۲۰: حمله به برج‌های دوقلوی مرکز تجارت جهانی
شهریور ۲۱: روز سینما
شهریور ۲۲: به قتل رسیدن مهسا امینی توسط جمهوری اسلامی در سال ۱۴۰۱ و شروع اعتراضات سراسری (زن، زندگی، آزادی) - روز گرامیداشت برنامه نویسان
شهریور ۲۷: روز شعر و ادب پارسی و روز بزرگداشت استاد شهریار
شهریور ۳۰: روز جهانی صلح
شهریور ۳۱: آغاز هفته دفاع مقدس
```


## Contribute <a class="anchor" id="cont"></a>
To contribute to this project, you can simply do so by making modifications and then making a `merge request`.
For now this is a simple project and I have these ideas for development:

 * `Adding Lunar date (Qamari) events to the events function`
 * `Add more formats to the now function`
 * `Age calculation by Jalali's date of birth`
 * `Convert English numbers to Farsi and vice versa`
 

## Resources <a class="anchor" id="res"></a>
Converting Gregorian date to Jalali date and vice versa: https://jdf.scr.ir/jdf/python

Events of Jalali history:
https://www.time.ir

