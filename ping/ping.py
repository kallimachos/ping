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


def square(x):
    """Square x.

    :param x: number to square
    :type x: int
    :returns: square of x
    :rtype: int

    >>> square(5)
    25
    """
    return x * x


if __name__ == "__main__":
    print(square(5))
