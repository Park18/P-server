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
#   - 이벤트 게시판 페이지: http://www.gong-cha.co.kr/brand/board/event.php?status=ing
#   - 이벤트 url: http://www.gong-cha.co.kr/brand/board/view.php?b=event&n=30231&status=ing&page=1
#   - 이벤트 사진: http://www.gong-cha.co.kr//uploads/board/20210127/084GXObu7VPE9eAn_20210127.png
#
# TODO
#   - DB 선택 및 추출한 데이터 DB에 넣는 처리
#   - 추출한 이미지를 저장해야 하는가 이미지 url을 이용해야 하는가 
###############################################################

from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request

BASE = "http://www.gong-cha.co.kr"
EVENT = "http://www.gong-cha.co.kr/brand/board/event.php?status=ing"

RESPONSE = urlopen(EVENT)
SOUP = BeautifulSoup(RESPONSE, 'html.parser')

def crawling():
    url()
    image()
    title()
    date()

def url():
    for anchor  in SOUP.select("div.imgs > a"):
        # 테스트
        print(BASE + anchor.get("href"))

        # TODO: DB push

def image():
    for anchor in SOUP.select("div.imgs > a > img"):
        img_url = BASE + anchor.get("src")
        print(img_url)

        # TODO: DB push

def title():
    for anchor in SOUP.select("p.tit"):
        print(anchor.get_text())

        # TODO: DB push

def date():
    # TODO: 기간이 존재하지 않은 이벤트가 있기 때문에 순서의 오류 발생 가능
    for anchor in SOUP.select("p.date"):
        print(anchor.get_text())

        # TODO: DB push
