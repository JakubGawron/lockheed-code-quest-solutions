import sys

input = lambda: sys.stdin.readline().rstrip()
# import math
# import string
# import re
from calendar import monthcalendar
from datetime import date, timedelta


def get_holidays(y):
    def get_weekday_date(m, day, i):
        cal = monthcalendar(y, m)
        return date(y, m, [week[day] for week in cal if week[day] != 0][i])

    holidays = [
        date(y, 11, 1),
        date(y, 4, 25),
        date(y, 12, 25),
        date(y, 10, 15),
        date(y, 8, 9),
        date(y, 1, 1),
        get_weekday_date(10, 0, 1),
        get_weekday_date(11, 6, 0),
        get_weekday_date(5, 0, -1),
        get_weekday_date(8, 0, -1),
        get_weekday_date(11, 3, 3),
        get_weekday_date(11, 3, 3) + timedelta(days=1),
    ]
    for i, holiday in enumerate(holidays):
        day = holiday.weekday()
        if day == 5:
            holidays[i] -= timedelta(days=1)
        elif day == 6:
            holidays[i] += timedelta(days=1)
    return holidays


for _ in range(int(input())):
    event_date, mode, days = input().split()
    event_date = date(*map(int, event_date.split("/")))
    days = int(days)
    direction = 1 if mode == "AFTER" else -1
    cdrl = event_date + direction * timedelta(days=days)
    holidays = [
        holiday
        for y in (cdrl.year, cdrl.year + direction)
        for holiday in get_holidays(y)
    ]
    a = 0
    while cdrl in holidays or cdrl.weekday() >= 5:
        cdrl += direction * timedelta(days=1)
        a += 1
    output = date.strftime(cdrl, "%Y/%m/%d")
    if a != 0:
        output += (
            " ADJUSTED "
            + ("+ " if direction == 1 else "- ")
            + str(a)
            + " DAY"
            + ("S" if abs(a) != 1 else "")
        )
    print(output)
