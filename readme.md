# 最終的なゴール

カレンダーで場所と日付のセレクトボックスを作成して、それで選択した情報に基づいてライブのスケジュールを表示する。

# 現在の進捗

- Zepp Namba のスケジュールをスクレイピングするスクリプトを作成
- そのスクリプトの取得結果を Json でリターンする API を作成

# 操作方法

## Python

- まずは仮想環境に入るために以下のコマンドを実行
  - `source python_12_venv/bin/activate`
- 初回起動時であればパッケージをインストール
  - `cd WebScrapingAPI`
  - `pip install -r requirements.txt`
- 以下コマンドで API 用の Flask サーバーを起動
  - `python liveCalendar`

# 学び

## Docker

- devcontainer.json
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

## VS Code

## Python

## React
