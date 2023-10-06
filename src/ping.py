#!/usr/bin/env python3
"""Test internet connection."""

from datetime import datetime
from pathlib import Path
from time import sleep

import requests


def print_write(msg: str) -> None:
    """Write message to result file."""
    print(msg)
    filepath = Path(Path(__file__).absolute().parent, "results.txt")
    with filepath.open(mode="a") as f:
        f.write(f"{msg}\n")
    return


def ping() -> None:
    """Test internet connection."""
    passmsg = f"Pass: {datetime.now()}"
    failmsg = f"Fail: {datetime.now()}"
    failing = False
    print_write(f"Start: {datetime.now()}")
    with requests.Session() as session:
        while True:
            passmsg = f"Pass: {datetime.now()}"
            failmsg = f"Fail: {datetime.now()}"
            try:
                if session.get("https://8.8.8.8"):
                    if failing is True:
                        print_write(passmsg)
                        failing = False
                elif failing is False:
                    print_write(failmsg)
                    failing = True
                sleep(10)
            except KeyboardInterrupt:
                print()
                return
            except Exception:
                if failing is False:
                    print_write(failmsg)
                    failing = True
    return


if __name__ == "__main__":
    ping()
