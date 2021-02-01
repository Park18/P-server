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
#   - 이벤트 게시판 1페이지: https://www.twosome.co.kr:7009/event/list.asp
#   - 이벤트 url: https://www.twosome.co.kr:7009/event/view.asp?idx=450&queryString=
#   - 이벤트 사진: https://www.twosome.co.kr:7009/Twosome_file/TWOSOME_EVENT_BBS/450_img01
#
# TODO
#   - DB 선택 및 추출한 데이터 DB에 넣는 처리
#   - 추출한 이미지를 저장해야 하는가 이미지 url을 이용해야 하는가 
###############################################################

from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request

from dir_manager import create_file

BASE = "https://www.twosome.co.kr:7009"
EVENT = "https://www.twosome.co.kr:7009/event/list.asp"

RESPONSE = urlopen(EVENT)
SOUP = BeautifulSoup(RESPONSE, 'html.parser')

def crawling():
    # url() # 자바스크립트 링크
    image()
    title()
    date()

def url():
    # TODO: 링크가 자바스크립트로 실행됨
    for anchor  in SOUP.select("div.event_listBox > a"):
        # 테스트
        print(anchor.get("onclick"))

        # TODO: DB push

def image():
    for anchor in SOUP.select("p.event-thumb > a > img"):
        img_url = BASE + anchor.get("src")
        print(img_url)

        # TODO: DB push

def title():
    for anchor in SOUP.select("div.event-cont > dl > dt"):
        print(anchor.get_text())

        # TODO: DB push

def date():
    for anchor in SOUP.select("dd.date"):
        print(anchor.get_text().strip())

        # TODO: DB push
