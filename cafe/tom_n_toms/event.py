###############################################################
# 이벤트 처리 클래스
###############################################################
#
# 이벤트 추출 리스트
#   - 이벤트 url
#   - 이벤트 이미지
#   - 이벤트 제목
#   - 등록일
#
# 이벤트 크롤링 관련 정보
#   - 이벤트 게시판 1페이지: https://tomntoms.com/event/event.html
#   - 이벤트 게시판 2페이지: https://tomntoms.com/event/event.html?page=2&plist=&find_field=&find_word=&find_state=&find_ordby=&conf=&mode=
#   - 이벤트 url: https://tomntoms.com/event/event.html?bmain=view&uid=27&mode=
#   - 이벤트 사진: https://tomntoms.com/upload/event/3067999205_eDomKczT_20210115042206.jpg
#
# TODO
#   - DB 선택 및 추출한 데이터 DB에 넣는 처리
#   - 추출한 이미지를 저장해야 하는가 이미지 url을 이용해야 하는가 
###############################################################

from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request

from dir_manager import create_file

BASE = "https://tomntoms.com"
EVENT = "https://tomntoms.com/event/event.html"

# https://tomntoms.com/upload/event/3067999205_eDomKczT_20210115042206.jpg
# background-image: url(/upload/event/3067999205_eDomKczT_20210115042206.jpg)
# 12345678901234567890123456789012345678901234567890123456789012345678901234567890

RESPONSE = urlopen(EVENT)
SOUP = BeautifulSoup(RESPONSE, 'html.parser')

def crawling():
    url()
    image()
    title()
    date()

def url():
    for anchor  in SOUP.select("div.event-list-item > a"):
        # 테스트
        print(BASE + anchor.get("href"))

        # TODO: DB push

def image():
    for anchor in SOUP.select("div.img-bx"):
        img_url = BASE + anchor.get("style")[22:74]
        print(img_url)

        # TODO: DB push

def title():
    for anchor in SOUP.select("p.tit"):
        print(anchor.get_text())

        # TODO: DB push

def date():
    for anchor in SOUP.select("p.date"):
        print(anchor.get_text().strip())

        # TODO: DB push
