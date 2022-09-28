import requests
from bs4 import BeautifulSoup 

url = "https://comic.naver.com/webtoon/list?titleId=675554"

res =requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# cartoons = soup.find_all("td",attrs={"class":"title"})
# title = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(title) 
# print("comic.naver.com" + link)

# 만화 제목 + 링크 구하기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link ="http://comic.naver.com" + cartoon.a["href"]
#     print(title,link)

# 평점 구하기
totla_rates = 0
cartoons = soup.find_all("div",attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    totla_rates += float(rate)
print("전체점수 : ",totla_rates)
print("평균점수 : ",totla_rates / len(cartoons))