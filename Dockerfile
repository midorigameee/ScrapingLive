# ベースイメージをUbuntuに指定
FROM ubuntu:24.04

RUN apt-get update

RUN apt-get install -y \
    vim \
    git \
    language-pack-ja-base language-pack-ja

RUN apt-get install -y python3 python3-pip
RUN apt-get install -y python3.12-venv
RUN apt-get install -y nodejs npm

# bashの日本語対応
ENV LC_ALL=ja_JP.UTF-8

# Gitの設定
RUN git config --global core.pager "LESSCHARSET=utf-8 less"
RUN git config --global --add --bool push.autoSetupRemote true