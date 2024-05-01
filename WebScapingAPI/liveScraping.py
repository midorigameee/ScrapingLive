import requests
from bs4 import BeautifulSoup

def getScheduleFromZeppNamba(target_date):
    t_year, t_month, t_day = map(int, target_date.split("/"))   # 01を1として扱うために一度intに変換する

    url = "https://www.zepp.co.jp/hall/namba/schedule/"
    param = "?" +  "_y=" + str(t_year) + "&" + "_m=" + str(t_month)
    url += param
    print("URL : " + url)

    res = requests.get(url)
    print("CONNECTION : " + str(res.status_code))

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
            return performer, title

    print("FIND RESULT : NOT FOUND")
    return None


def main():
    target_date = "2024/05/3"
    performer, title = getScheduleFromZeppNamba(target_date)
    print(performer+"「" + title + "」")


if __name__ == "__main__":
    main()