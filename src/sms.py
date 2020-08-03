#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Send an sms using Twilio."""

from os import getenv

from dotenv import find_dotenv, load_dotenv
from twilio.rest import Client

load_dotenv(find_dotenv())
twilio_sid = getenv("TWILIO_SID")
twilio_token = getenv("TWILIO_TOKEN")
twilio_num = getenv("TWILIO_NUM")
mobile_num = getenv("MOBILE_NUM")


def send_sms(msg):
    """Send an sms."""
    client = Client(twilio_sid, twilio_token)
    message = client.messages.create(body=msg, from_=twilio_num, to=mobile_num)
    return message.sid


if __name__ == "__main__":
    send_sms("Testing")
