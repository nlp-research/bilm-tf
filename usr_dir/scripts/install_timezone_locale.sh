#!/bin/bash
apt update && apt install -y --no-install-recommends \
    locales \
    tzdata \
    vim
apt clean

locale-gen ko_KR.UTF-8
export LANG=ko_KR.UTF-8 LC_MESSAGES=POSIX

export TZ=Asia/Seoul
mv /etc/localtime /etc/localtime.bak
ln -s /usr/share/zoneinfo/$TZ /etc/localtime
echo $TZ > /etc/timezone