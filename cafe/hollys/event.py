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
#   - 이벤트 게시판 1페이지: https://www.hollys.co.kr/news/event/list.do
#   - 이벤트 게시판 2페이지: https://www.hollys.co.kr/news/event/list.do?pageNo=2&closeYn=&division=
#   - 이벤트 url: https://www.hollys.co.kr/news/event/view.do?idx=251&pageNo=1&division=
#   - 이벤트 사진: http://admin.hollys.co.kr/upload/news/event/newsEvent_202101110141114930.jpg
#
# TODO
#   - DB 선택 및 추출한 데이터 DB에 넣는 처리
#   - 추출한 이미지를 저장해야 하는가 이미지 url을 이용해야 하는가 
###############################################################

from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request

EVENT = "https://www.hollys.co.kr/news/event/list.do"

RESPONSE = urlopen(EVENT)
SOUP = BeautifulSoup(RESPONSE, 'html.parser')

def crawling():
    # url()
    image()
    title()
    date()

def url():
    # TODO: 인벤트 url이 자바스크립트로 작동함
    for anchor  in SOUP.select("div.event_listBox > a"):
        # 테스트
        print(anchor.get("onclick"))

        # TODO: DB push

def image():
    for anchor in SOUP.select("div.event_listBox > a > img"):
        img_url = anchor.get("src")[2:]
        print(img_url)

        # TODO: DB push

def title():
    for anchor in SOUP.select("dd.pad_l_15"):
        print(anchor.get_text())

        # TODO: DB push

def date():
    for anchor in SOUP.select("dd.event_date"):
        print(anchor.get_text()[5:])

        # TODO: DB push
