from flask import Flask, render_template, Response, request
from flask_cors import CORS
from scrapeLiveInfo import ZeppNamba
import sys


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    # カレンダーを表示するためのテンプレートをレンダリング
    return render_template('calendar.html')

@app.route('/api/osaka/zepp-namba', methods=['GET'])
def getZeppNamba():
    try:
        req = request.args
        yaer = req.get("year")
        month = req.get("month")
        day = req.get("day")
        if yaer == "" or month == "" or day == "":
            target_date = ""
        else:
            target_date = yaer+"/"+month+"/"+day
    except Exception as e:
        target_date = ""
        pass
    finally:
        zn = ZeppNamba()
        json_data = zn.getLiveInfoJson(target_date)
        response = Response(json_data, content_type='application/json')
        return response

if __name__ == '__main__':
    portNo = 5000

    # 開発環境の時は引数でポートを5001にする
    args = sys.argv
    if len(args) > 1:
        portNo = int(args[1])

    app.run(host='0.0.0.0',debug=True, port=portNo)