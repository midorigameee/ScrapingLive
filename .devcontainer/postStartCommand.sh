#!/bin/sh

touch ~/.bash_aliases
cat /workspaces/ScrapingLive/.devcontainer/bash_aliases > ~/.bash_aliases

# Gitのブランチを表示させる設定
curl -o git-prompt.sh https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh
mv git-prompt.sh ~
