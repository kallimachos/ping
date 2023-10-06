#!/usr/bin/env python3
"""Calculate downtime."""

from datetime import datetime, timedelta
from pathlib import Path


def diff(fail: str, padd: str) -> timedelta:
    """Calculate the diff in minutes between a Fail and Pass event."""
    failtime = datetime.strptime(fail.strip("Fail: ").strip(), "%Y-%m-%d %H:%M:%S.%f")
    passtime = datetime.strptime(padd.strip("Pass: ").strip(), "%Y-%m-%d %H:%M:%S.%f")
    return passtime - failtime


def downtime() -> tuple:
    """Calculate the total downtime."""
    filepath = Path(Path(__file__).absolute().parent, "results.txt")
    fails = 0
    time = timedelta()
    with filepath.open() as f:
        next(f)
        for line in f:
            fail = line
            padd = next(f)
            fails += 1
            time += diff(fail, padd)
    return (fails, time)


def get_start() -> datetime:
    """Return start datetime."""
    filepath = Path(Path(__file__).absolute().parent, "results.txt")
    with filepath.open() as f:
        start = f.readline()
    return datetime.strptime(start.strip("Start: ").strip(), "%Y-%m-%d %H:%M:%S.%f")


def uptime(start: datetime, downtime: timedelta) -> tuple:
    """Calculate number of days tracked and determine uptime."""
    today = datetime.today()
    days = today - start
    percentage = f"{(100 - (downtime / days * 100)):.2f}"
    return (str(today.date()), str(days.days), percentage)


if __name__ == "__main__":
    start = get_start()
    startdate = str(start.date())
    fails, timedown = downtime()
    today, days, timeup = uptime(start, timedown)
    print(f"\n{'From':<15}{'To':<15}{'Days':<10}{'Fails':<10}{'Downtime':<30}Uptime")
    print(f"{startdate:<15}{today:<15}{days:<10}{fails:<10}{timedown!s:<30}{timeup}%\n")
