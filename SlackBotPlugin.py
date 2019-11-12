# -*- coding: utf-8 -*-

from slackbot.bot import respond_to, listen_to
import re
import subprocess


# グローバル定数
EXEC_ANNOUNCE = "/usr/share/pi-jtalk/bin/announce.sh"

# !announce 指定されたメッセージを発話する
@respond_to('^!announce (.*)')
def announce(message, something):
    subprocess.call([EXEC_ANNOUNCE, something])

# !announce_if_in_time hh-hh hh-hh時間内なら指定メッセージを発話する
@respond_to('^!announce_if_in_time ([0-2][0-9]-[0-2][0-9]) (.*)')
def announce_if_in_time(message, time, something):
    # TODO: 時刻の解析
    in_time = True

    if (in_time):
        announce(message, something)