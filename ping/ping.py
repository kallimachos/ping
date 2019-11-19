#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ping source file.

https://github.com/kallimachos/ping

Copyright (C) 2019 Brian Moss

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from datetime import datetime
from time import sleep

from requests import get

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
                time = False
        else:
            if time is False:
                print(f"Fail: {datetime.now()}")
                time = True
        sleep(10)
    except Exception:
        if time is False:
            print(f"Fail: {datetime.now()}")
            time = True
