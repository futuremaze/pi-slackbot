# -*- coding: utf-8 -*-

from slackbot.bot import respond_to, listen_to
import re
import subprocess
import datetime

# グローバル定数
EXEC_ANNOUNCE = "/usr/share/pi-jtalk/bin/announce.sh"

# !announce 指定されたメッセージを発話する
@respond_to('^!announce (.*)')
def announce(message, something):
    subprocess.call([EXEC_ANNOUNCE, something])
    message.reply("メッセージを再生しました")

# !announce_if_in_time hh-hh hh-hh時間内なら指定メッセージを発話する
@respond_to('^!announce_if_in_time ([0-2]{0,1}[0-9]-[0-2][0-9]) (.*)')
def announce_if_in_time(message, time, something):
    now = datetime.datetime.now()
    time_s = time.split('-')
    start, end = int(time_s[0]), int(time_s[1])

    if (start <= now.hour and end >= now.hour):
        announce(message, something)
