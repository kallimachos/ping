#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Send an email. Note: requires a running smtp server on localhost."""

import smtplib
from email.message import EmailMessage


def send_email(msg):
    """Send an email."""
    msg = EmailMessage()
    msg.set_content(msg)
    msg["Subject"] = "An email message"
    msg["From"] = "kallimachos@gmail.com"
    msg["To"] = "kallimachos@gmail.com"

    # Send the message via our own SMTP server.
    s = smtplib.SMTP("localhost", 1025)
    s.send_message(msg)
    s.quit()


if __name__ == "__main__":
    send_email("hello world")
