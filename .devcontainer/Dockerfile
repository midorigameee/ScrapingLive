# ベースイメージをPythonのAlpine Linuxに指定
FROM ubuntu:24.04

RUN apt-get update && apt-get install -y \
    git \
    python3 \
    python3-pip \
    nodejs \
    npm

# Pythonのバージョン確認
RUN python3 --version

# Node.jsのバージョン確認
RUN node --version