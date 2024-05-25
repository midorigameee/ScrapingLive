from flask import Flask, render_template, Response, request
from flask_cors import CORS
from scrapeLiveInfo import ZeppNamba
import sys
from scrapingAPIs.zepp import Zepp


app = Flask(__name__)
CORS(app)


def validateDateParameters(yaer, month, day):
    target_date = ""

    if yaer != "" and month != "" and day != "":
        target_date = yaer+"/"+month+"/"+day
    
    return target_date

@app.route('/')
def index():
    # カレンダーを表示するためのテンプレートをレンダリング
    return render_template('calendar.html')


@app.route('/api/osaka', methods=['GET'])
def getLiveInfoOsaka():
    try:
        req = request.args
        yaer = req.get("year")
        month = req.get("month")
        day = req.get("day")
        target_date = validateDateParameters(yaer, month, day)
    except Exception as e:
        target_date = ""
        pass
    finally:
        zepp_namba = Zepp(url="https://www.zepp.co.jp/hall/namba/schedule/", area="大阪", site="Zepp Namba")
        json_data = zepp_namba.getLiveInfoJson(target_date)
        response = Response(json_data, content_type='application/json')
        return response


@app.route('/api/nagoya', methods=['GET'])
def getLiveInfoNagoya():
    try:
        req = request.args
        yaer = req.get("year")
        month = req.get("month")
        day = req.get("day")
        target_date = validateDateParameters(yaer, month, day)
    except Exception as e:
        target_date = ""
        pass
    finally:
        zepp_nagoya = Zepp(url="https://www.zepp.co.jp/hall/nagoya/schedule/", area="名古屋", site="Zepp Nagoya")
        json_data = zepp_nagoya.getLiveInfoJson(target_date)
        response = Response(json_data, content_type='application/json')
        return response


@app.route('/api/tokyo', methods=['GET'])
def getLiveInfoTokyo():
    try:
        req = request.args
        yaer = req.get("year")
        month = req.get("month")
        day = req.get("day")
        target_date = validateDateParameters(yaer, month, day)
    except Exception as e:
        target_date = ""
        pass
    finally:
        zepp_shinjuku = Zepp(url="https://www.zepp.co.jp/hall/shinjuku/schedule/", area="東京", site="Zepp Shinjuku")
        json_data = zepp_shinjuku.getLiveInfoJson(target_date)
        response = Response(json_data, content_type='application/json')
        return response


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