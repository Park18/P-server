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
#   - 이벤트 게시판 1페이지: http://www.no1juicy.com/bbs/board/lists/?bo_table=event
#   - 이벤트 게시판 2페이지: http://www.no1juicy.com/bbs/board/lists/2?bo_table=event
#   - 이벤트 url: http://www.no1juicy.com/bbs/board/view?bo_table=event&wr_id=82
#   - 이벤트 사진: http://www.no1juicy.com/uploads/board/event/82/thumb/cedcfaf0213b23e792b6d1d49bf90d23.png
#
# TODO
#   - DB 선택 및 추출한 데이터 DB에 넣는 처리
#   - 추출한 이미지를 저장해야 하는가 이미지 url을 이용해야 하는가 
###############################################################

import os # 실행 위치

from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request

from dir_manager import create_file

BASE = "http://www.no1juicy.com"
EVENT = "http://www.no1juicy.com/bbs/board/lists?bo_table=event"

class Event:
    def __init__(self):
        self.response = urlopen(EVENT)
        self.soup = BeautifulSoup(self.response, 'html.parser')

    def crawling(self):
        self.url()
        self.image()
        self.title()
        self.date()

    def url(self):
        for anchor  in self.soup.select("ul.ntcList > li > a"):
            # 테스트
            print(BASE + anchor.get("href"))

            # TODO: DB push

    def image(self):
        for anchor in self.soup.select("ul.ntcList > li > a > img"):
            img_url = BASE + anchor.get("src")
            print(img_url)

            # TODO: DB push

    def title(self):
        for anchor in self.soup.select("ul.ntcList > li > a > dl > dt"):
            print(anchor.get_text())

            # TODO: DB push

    def date(self):
        for anchor in self.soup.select("ul.ntcList > li > a > dl > dd:nth-child(3)"):
            print(anchor.get_text())

            # TODO: DB push
