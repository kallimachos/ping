#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Run speedtest-cli and print result."""

import subprocess
from codetiming import Timer
from yaspin import yaspin


def speedtest():
    """Run speedtest."""
    response = (
        subprocess.Popen(
            "/usr/local/bin/speedtest-cli --simple", shell=True, stdout=subprocess.PIPE
        )
        .stdout.read()
        .decode("utf-8")
    )
    return response


if __name__ == "__main__":
    with Timer(text="\033[32mElapsed time: {:0.2f} seconds\033[0m\n"):
        with yaspin(text=f"Running speedtest", color="green") as spinner:
            response = speedtest()
            spinner.ok()
        print(f"\n{response}")
