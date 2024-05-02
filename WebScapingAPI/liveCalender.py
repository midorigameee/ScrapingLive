from flask import Flask, render_template, Response
from scrapeLiveInfo import ZeepNamba

app = Flask(__name__)

@app.route('/')
def index():
    # カレンダーを表示するためのテンプレートをレンダリング
    return render_template('calendar.html')

@app.route('/api/osaka/zepp-namba', methods=['GET'])
def getZeppNamba():
    zn = ZeepNamba()
    json_data = zn.getLiveInfoJson()
    response = Response(json_data, content_type='application/json')
    return response

if __name__ == '__main__':
    app.run(debug=True)