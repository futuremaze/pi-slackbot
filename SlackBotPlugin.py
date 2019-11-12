# -*- coding: utf-8 -*-

from slackbot.bot import respond_to, listen_to
import re
import subprocess


EXEC_ANNOUNCE = "/usr/share/pi-jtalk/bin/announce.sh"

# !announce 指定されたメッセージを発話する
@respond_to('^.*!announce (.*)')
def announce(message, something):
    subprocess.call([EXEC_ANNOUNCE, something])

