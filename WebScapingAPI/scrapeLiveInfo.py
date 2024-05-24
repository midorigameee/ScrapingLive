import requests
from bs4 import BeautifulSoup
import json
import ast

class ZeppNamba:
    def __init__(self):
        self.url = "https://www.zepp.co.jp/hall/namba/schedule/"
        self.area = "大阪"
        self.site = "Zeep Namba"
        self.result = False

    def convertJson(self, result, target_date, performer, title, area, site):
        data = {
            "result": result,
            "date": target_date,
            "performer": performer,
            "title": title,
            "area": area,
            "site": site
        }

        json_data = json.dumps(data, ensure_ascii=False)
        return json_data


    def getLiveInfoJson(self, target_date):
        if target_date is None or target_date == "":
            from datetime import date
            today = date.today()
            target_date = today.strftime("%Y/%m/%d")

        performer, title = self.fetchSchedule(target_date)
        
        json_data = self.convertJson(self.result, target_date, performer, title, self.area, self.site)
        return json_data


    def createURL(self, t_year, t_month):
        param = "?" +  "_y=" + str(t_year) + "&" + "_m=" + str(t_month)
        url = self.url +param
        return url


    def fetchSchedule(self, target_date):
        print("===== fetchSchedule =====")
        # 日付の01を1に変換するために一度intに変換する
        t_year, t_month, t_day = map(int, target_date.split("/"))
        url = self.createURL(t_year, t_month)

        try:
            res = requests.get(url)
            print("URL : " + url)
            print("CONNECTION : " + str(res.status_code))

            if res.status_code != 200:
                return "Status code is not 200", str(res.status_code)

            soup = BeautifulSoup(res.text, "html.parser")
            elems = soup.find_all("a", class_="sch-content")

            for content in elems:
                month_and_date = content.find("p", class_="sch-content-date__month")

                if month_and_date is None:
                    continue

                month = month_and_date.string.split(".")[0]    # タグの間のテキストコンテンツを取得するためには.stringが必要
                date = month_and_date.string.split(".")[1]

                if month == str(t_month) and date == str(t_day):
                    performer = content.find("h2", class_="sch-content-text__performer").string
                    title = content.find("h3", class_="sch-content-text__ttl").string

                    print("FIND RESULT : FOUND")
                    print("CONTENT : " + performer+"「" + title + "」")
                    print("===== ===== ===== =====")

                    self.result = True
                    return performer, title

            print("FIND RESULT : NOT FOUND")
            print("===== ===== =====")
            return "", ""
                
        except Exception as e:
            print("エラー : ",e)
            print("FIND RESULT : NOT FOUND")
            print("===== ===== =====")
            return e, ""