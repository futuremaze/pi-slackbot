# -*- coding: utf-8 -*-

import os

API_TOKEN = os.environ['SLACK_API_TOKEN']

# デフォルトの返答
default_reply = 'すみません、よくわかりません。'

# プラグインを記述するパッケージ名のリスト
PLUGINS = [
    'plugins',
]