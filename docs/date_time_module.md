# Simple Examples of Python3 datetime module

```python3
#!/usr/bin/env python3
"""main.py"""
import datetime


def f_one():
    today = datetime.datetime.today()
    now = datetime.datetime.now()
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    strf_one = datetime.datetime.now().strftime("%x %X")

    print(f"{today = }")
    print(f"{now = }")
    print(f"{year = }")
    print(f"{month = }")
    print(f"{day = }")
    print(f"{hour = }")
    print(f"{minute = }")
    print(f"{second = }")
    print(f"{strf_one = }")
    print(f"{year}-{month}-{day}T{hour}:{minute}:{second}")


def f_two():
    print(datetime.date.today())
    print(datetime.date.fromisocalendar(year=2023, week=45, day=7))


f_one()
f_two()
```
