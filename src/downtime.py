#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Calculate downtime."""

from datetime import datetime, timedelta
from os import path
from pathlib import Path


def diff(Fail, Pass):
    """Calculate the diff in minutes between a Fail and Pass event."""
    Fail = datetime.strptime(Fail.strip("Fail: ").strip(), "%Y-%m-%d %H:%M:%S.%f")
    Pass = datetime.strptime(Pass.strip("Pass: ").strip(), "%Y-%m-%d %H:%M:%S.%f")
    difference = Pass - Fail
    return difference


def downtime():
    """Calculate the total downtime."""
    filepath = path.join(Path(__file__).absolute().parent, "results.txt")
    fails = 0
    time = timedelta()
    with open(filepath, "r") as f:
        for line in f:
            Fail = line
            Pass = next(f)
            fails += 1
            time += diff(Fail, Pass)
    return (fails, time)


def uptime(downtime):
    """Calculate number of days tracked and determine uptime."""
    today = datetime.today()
    days = today - datetime.strptime("2019-11-15", "%Y-%m-%d")
    percentage = f"{(100 - (downtime / days * 100)):.2f}"
    return (str(today.date()), str(days.days), percentage)


if __name__ == "__main__":
    fails, downtime = downtime()
    today, days, uptime = uptime(downtime)
    print(f"\n{'From':<15}{'To':<15}{'Days':<10}{'Fails':<10}{'Downtime':<30}Uptime")
    print(f"{'2019-11-15':<15}{today:<15}{days:<10}{fails:<10}{str(downtime):<30}{uptime}%\n")
