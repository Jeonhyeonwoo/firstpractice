import re
import requests
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    return soup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)
    # 흐림 어제보다 ㅇㅇ 높아요
    cast = soup.find("p",attrs={"class":"summary"}).get_text()
    # 현재 ㅁㅁ 도 (최저 ㅁㅁ/ 최고 ㅁㅁ)
    curr_temp = soup.find("div",attrs={"class":"temperature_text"}).get_text() #현재온도
    min_temp = soup.find("span",attrs={"class":"lowest"}).get_text() #최저온도
    max_temp = soup.find("span",attrs={"class":"highest"}).get_text()
    # 강수확률 ㅁㅁ %
    rain_rate = soup.find_all("span",attrs={"class":"rainfall"})
    morning_rainrate = rain_rate[0].get_text()
    afternoon_rainrate = rain_rate[1].get_text()
    #미세먼지
    dust = soup.find_all("span",attrs={"class":"txt"})
    pm10 = dust[0].get_text()
    pm25 = dust[1].get_text()
    
    
    print(cast)
    print("현재",curr_temp[6:],"(최저",min_temp[4:],"/ 최고",max_temp[4:],")")
    print("오전 강수확률",morning_rainrate,"/ 오후 강수확률",afternoon_rainrate)
    print("미세먼지 : ",pm10,"/초미세먼지 : ",pm25)
    print()
    
def scrape_healine_news():
    print("[언론사별 가장 많이 본 뉴스]")
    url = "https://news.naver.com/main/officeList.naver"
    soup = create_soup(url)
    news_list = soup.find("ul",attrs={"class":"section_list_ranking_press _rankingList"}).find_all("li")
    for index ,news in enumerate(news_list):
        title = news.get_text().strip()
        link = "https://news.naver.com" + news.find("div",attrs={"class":"list_text_inner"}).find("a")["href"]
        print("{}. {}".format(index+1,title))
        print("링크 : "+link)
    print()

def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    news_list = soup.find("ul",attrs={"class":"type06_headline"}).find_all("li",limit=3)
    for index , news in enumerate(news_list):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1 #이미지가 있으면 1번째 img 태그의 정보를 사용

        a_tag = news.find_all("a")[a_idx]
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        print("{}. {}".format(index+1,title))
        print("링크 : "+link)
    print()

def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english#;"
    soup = create_soup(url)
    sentences = soup.find_all("div",attrs={"id":re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]: # 8문장이 있다고 가정할때 index 기준 4~7 까지 잘라서 가져옴
        print(sentence.get_text().strip())
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]: # 8문장이 있다고 가정할때 index 기준 4~7 까지 잘라서 가져옴
        print(sentence.get_text().strip())


    print()

if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_healine_news() #언론사별 가장 많이 본 뉴스 가져오기
    scrape_it_news() #IT 뉴스 정보 가져오기
    scrape_english() #오늘의 영어 회화 가져오기