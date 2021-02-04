###############################################################
# 이벤트 처리 클래스
###############################################################
#
# 이벤트 추출 리스트
#   - 이벤트 url
#   - 이벤트 제목
#   - 등록일
#
# 이벤트 크롤링 관련 정보
#   - 이벤트 게시판 1페이지: http://paikdabang.com/news/?cate=event
#   - 이벤트 게시판 2페이지: http://paikdabang.com/news/page/2/?cate=event
#   - 이벤트 url: http://paikdabang.com/post_news/%eb%b9%bd%eb%8b%a4%eb%b0%a9%eb%a9%a4%eb%b2%84%ec%8b%ad-%eb%8d%94-%ea%b0%95%eb%a0%a5%ed%95%b4%ec%a7%84-%ea%bd%9d%ec%97%86%eb%8a%94-%ec%9d%b4%eb%b2%a4%ed%8a%b8-%ec%b0%b8%ec%97%ac%ed%95%98/
#   
# TODO
#   - DB 선택 및 추출한 데이터 DB에 넣는 처리
###############################################################

from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request

EVENT = "http://paikdabang.com/news/?cate=event"

RESPONSE = urlopen(EVENT)
SOUP = BeautifulSoup(RESPONSE, 'html.parser')

def crawling():
    url()
    title()
    date()

def url():
    for anchor  in SOUP.select("td.tit > a"):
        # 테스트
        print(anchor.get("href"))

        # TODO: DB push

def title():
    for anchor in SOUP.select("td.tit > a"):
        print(anchor.get_text().strip())

        # TODO: DB push

def date():
    for anchor in SOUP.select("td.date"):
        print(anchor.get_text())

        # TODO: DB push