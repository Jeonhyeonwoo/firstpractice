import csv #쉼표 형태로 저장된 데이터
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = " 시가총액 1~200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
# ["N","종목명","현재가","전일비"....]
writer.writerow(title)

for page in range(1,2):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    data_rows = soup.find("table",attrs={"class":"type_2"}).find("tbody").find_all("tr")
    for row in data_rows:
        colums = row.find_all("td")
        if len(colums) <= 1: #의미 없는 data는 skip
            continue
        data = [column.get_text().strip() for column in colums]
        # print(data)
        writer.writerow(data)