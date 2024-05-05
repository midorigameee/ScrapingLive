from flask import Flask, render_template, Response, request
from scrapeLiveInfo import ZeepNamba

app = Flask(__name__)

@app.route('/')
def index():
    # カレンダーを表示するためのテンプレートをレンダリング
    return render_template('calendar.html')

@app.route('/api/osaka/zepp-namba', methods=['GET'])
def getZeppNamba():
    try:
        req = request.args
        yaer = req.get("yaer")
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
        zn = ZeepNamba()
        json_data = zn.getLiveInfoJson(target_date)
        response = Response(json_data, content_type='application/json')
        return response

if __name__ == '__main__':
    app.run(debug=True)