#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Run speedtest-cli and print result."""

import subprocess

response = (
    subprocess.Popen(
        "/usr/local/bin/speedtest-cli --simple", shell=True, stdout=subprocess.PIPE
    )
    .stdout.read()
    .decode("utf-8")
)
print(response)
