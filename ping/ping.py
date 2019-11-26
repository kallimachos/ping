#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test internet connection."""

from datetime import datetime
from os import path
from time import sleep

from git import Repo
from requests import get

import sms


def print_write(msg):
    """Write message to result file."""
    print(msg)
    repo_root = Repo(".", search_parent_directories=True).working_tree_dir
    filepath = path.abspath(path.join(repo_root, "ping/results.txt"))
    with open(filepath, "a") as f:
        f.write(f"{msg}\n")
    return


def ping():
    """Test internet connection."""
    passmsg = f"Pass: {datetime.now()}"
    failmsg = f"Fail: {datetime.now()}"
    try:
        if get("https://8.8.8.8"):
            print_write(passmsg)
            time = False
        else:
            print_write(failmsg)
            time = True
    except Exception:
        print_write(failmsg)
        time = True

    while True:
        passmsg = f"Pass: {datetime.now()}"
        failmsg = f"Fail: {datetime.now()}"
        try:
            if get("https://8.8.8.8"):
                if time is True:
                    print_write(passmsg)
                    sms.send_sms("Internet is up.")
                    time = False
            else:
                if time is False:
                    print_write(failmsg)
                    time = True
            sleep(10)
        except KeyboardInterrupt:
            print()
            return
        except Exception:
            if time is False:
                print_write(failmsg)
                time = True
    return


if __name__ == "__main__":
    ping()
