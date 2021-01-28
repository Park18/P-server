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
#   - 이벤트 게시판 1페이지: http://www.megacoffee.me/bbs/board.php?bo_table=event
#   - 이벤트 게시판 2페이지: http://www.megacoffee.me/bbs/board.php?bo_table=event&page=2
#   - 이벤트 url: http://www.megacoffee.me/bbs/board.php?bo_table=event&wr_id=307
#   
# TODO
#   - DB 선택 및 추출한 데이터 DB에 넣는 처리
###############################################################

from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request

EVENT = "http://www.megacoffee.me/bbs/board.php?bo_table=event"

class Event:
    def __init__(self):
        self.response = urlopen(EVENT)
        self.soup = BeautifulSoup(self.response, 'html.parser')

    def crawling(self):
        self.url()
        self.title()
        self.date()

    def url(self):
        for anchor  in self.soup.select("td.td_subject > a"):
            # 테스트
            print(anchor.get("href"))

            # TODO: DB push

    def title(self):
        for anchor in self.soup.select("td.td_subject > a"):
            print(anchor.get_text().strip())

            # TODO: DB push

    def date(self):
        for anchor in self.soup.select("td.td_date"):
            print(anchor.get_text())

            # TODO: DB push
