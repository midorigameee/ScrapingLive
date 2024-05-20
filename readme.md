# 最終的なゴール

カレンダーで場所と日付のセレクトボックスを作成して、それで選択した情報に基づいてライブのスケジュールを表示する。

# 現在の進捗

- Zepp Namba のスケジュールをスクレイピングするスクリプトを作成
- そのスクリプトの取得結果を Json でリターンする API を作成

# 環境について

## 開発環境

VS Code でコンテナ内にアクセスできるようにしている。

一応コンテナごとサーバーに持っていけるように

## 本番環境

Render にデプロイする。

FlaskAPI と WebAP でデプロイ先を分ける。

# 操作方法

## Python

- ~まずは仮想環境に入るために以下のコマンドを実行~
  - ~`source python_12_venv/bin/activate`~
- 仮想環境に自動で入るように`./bash_profile`に追加したので bash 起動時には仮想環境が立ち上がっている
- 初回起動時であればパッケージをインストール
  - `cd WebScrapingAPI`
  - `pip install -r requirements.txt`
- 以下コマンドで API 用の Flask サーバーを起動
  - `python liveCalendar`

## React

# 学び

## Docker

### devcontainer.json

- コンテナが作られる前に実行するコマンドは postCreateCommand として設定する
- prettier
  - インストール&保存時に自動適用
  ```
  "customizations": {
      "vscode": {
          "extensions": [
          "esbenp.prettier-vscode"
          ],
          "settings": {
           "editor.formatOnSave": true,
          "editor.defaultFormatter": "esbenp.prettier-vscode"
          }
      }
  }
  ```
- ポートの設定
  - `"forwardPorts": [5000]`

### Docker コンテナ内でもホストと同じ Git の SSH 認証を使う方法

- ホスト側に`.ssh/id_ed25519`を用意する
  - すでにホスト側では Git に SSH 接続できる前提
- ホスト（WSL）で以下のコマンドで ssh-agent を実行する
  - `` $ eval `ssh-agent`   ``
  - コンソール出力 `Agent pid 1611`
- ssh-agent に SSH キーを追加する
  - `ssh-add ~/.ssh/id_ed25519`
- これで Git に SSH 接続できるようになる
  - `$ ssh -T git@github.com` で疎通確認
  - コンソール出力`Hi <username>! You've successfully authenticated, but GitHub does not provide shell access.`
- `~/.bash_profile`に上記処理を常に実行する設定を追加する

```
  if [ -z "$SSH_AUTH_SOCK" ]; then
# Check for a currently running instance of the agent
RUNNING_AGENT="`ps -ax | grep 'ssh-agent -s' | grep -v grep | wc -l | tr -d '[:space:]'`"
if [ "$RUNNING_AGENT" = "0" ]; then # Launch a new instance of the agent
ssh-agent -s &> $HOME/.ssh/ssh-agent
fi
eval `cat $HOME/.ssh/id_ed25519`
fi

ssh-add $HOME/.ssh/id_rsa
```

- ターミナルを開きなおして、再度 VS Code を立ち上げてコンテナに接続する
  - コンテナ内で`$ ssh -T git@github.com` で疎通確認

## VS Code

## Python

## React
