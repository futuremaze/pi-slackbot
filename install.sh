#!/bin/bash

# bashのスイッチ
set -euC

# カレントディレクトリの移動
cd $(dirname $0)

# 外部スクリプトのsource
# source ./setting.inc

# グローバル定数
readonly INSTALL_DIR="/usr/share/pi-slackbot"

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

  sudo pip3 install --upgrade pip3
  sudo pip3 install slackbot

  # スクリプトのインストール
  sudo mkdir -p ${INSTALL_DIR}
  sudo cp -R ./bin ${INSTALL_DIR}/
}

# EXIT時にcleanup実行
trap cleanup EXIT

# エントリー処理
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  main
fi
