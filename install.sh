#!/bin/bash

# bashのスイッチ
set -euCx

# カレントディレクトリの移動
cd $(dirname $0)

# 外部スクリプトのsource
# source ./setting.inc

# グローバル定数
readonly INSTALL_DIR="/usr/local/pi-slackbot"

#
# 関数定義
#

function cleanup() {
  :
}

function main() {
  # 必要パッケージのダウンロード
  sudo apt-get install -y \
    python3-pip \
    python3-dev

  sudo pip3 install --upgrade pip
  sudo pip3 install slackbot

  # パッチ適用
  SLACKBOT_DIR="$(pip3 show slackbot | grep Location: | sed -e 's/^Location: //g')/slackbot"
  sudo patch -u ${SLACKBOT_DIR}/dispatcher.py < ./dispatcher.py.patch

  # スクリプトのインストール
  sudo mkdir -p ${INSTALL_DIR}
  sudo cp -R ./bin ${INSTALL_DIR}/

  # Service の設定
  sudo cp ./pi-slackbot.service /etc/systemd/system/
  sudo systemctl list-unit-files --type=service | grep pi-slackbot
  sudo systemctl enable pi-slackbot.service
  sudo systemctl start pi-slackbot.service
}

# EXIT時にcleanup実行
trap cleanup EXIT

# エントリー処理
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  main
fi
