#!/bin/python3
# coding: utf-8
"""ping test file."""

from ping import ping


def test_square():
    """Test square."""
    assert ping.square(1) == 1
    assert ping.square(2) == 4
    assert ping.square(3) == 9
    assert ping.square(4) == 16
    assert ping.square(5) == 25


if __name__ == "__main__":
    pass
