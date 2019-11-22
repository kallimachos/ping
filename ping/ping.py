#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test internet connection."""

from datetime import datetime
from time import sleep

from requests import get

import sms


def ping():
    """Test internet connection."""
    try:
        if get("https://8.8.8.8"):
            print(f"Pass: {datetime.now()}")
            time = False
        else:
            print(f"Fail: {datetime.now()}")
            time = True
    except Exception:
        print(f"Fail: {datetime.now()}")
        time = True

    while True:
        try:
            if get("https://8.8.8.8"):
                if time is True:
                    print(f"Pass: {datetime.now()}")
                    sms.send_sms("Internet is up.")
                    time = False
            else:
                if time is False:
                    print(f"Fail: {datetime.now()}")
                    time = True
            sleep(10)
        except KeyboardInterrupt:
            print()
            return
        except Exception:
            if time is False:
                print(f"Fail: {datetime.now()}")
                time = True
    return


if __name__ == "__main__":
    ping()
