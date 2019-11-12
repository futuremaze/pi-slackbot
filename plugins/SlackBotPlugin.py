# -*- coding: utf-8 -*-

from slackbot.bot import respond_to, listen_to
import re

# !announce 指定されたメッセージを発話する
@respond_to('^!announce (.*)')
def announce(command, message):
    print("command: " + command)
    print("message: " + message)
