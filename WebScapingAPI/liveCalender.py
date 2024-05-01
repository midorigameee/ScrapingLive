from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # カレンダーを表示するためのテンプレートをレンダリング
    return render_template('calendar.html')

if __name__ == '__main__':
    app.run(debug=True)