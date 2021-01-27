# 쥬씨 크롤링
# 이벤트
#   - 이벤트 세부 페이지 url
#   - 이미지
#   - 제목
#   - 등록일
# 이벤트 게시판 2페이지: "http://www.no1juicy.com/bbs/board/lists/2?bo_table=event"
# 이벤트 상세: http://www.no1juicy.com/bbs/board/view?bo_table=event&wr_id=82
# 이벤트 사진: http://www.no1juicy.com/uploads/board/event/82/thumb/cedcfaf0213b23e792b6d1d49bf90d23.png

import os # 실행 위치

from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request

BASE = "http://www.no1juicy.com"
EVENT = "http://www.no1juicy.com/bbs/board/lists?bo_table=event"

EVENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__)) + '/event/'

class Event:
    def __init__(self):
        self.response = urlopen(EVENT)
        self.soup = BeautifulSoup(self.response, 'html.parser')

    def crawling(self):
        #self.url()
        self.image()
        #self.title()
        #self.date()

        # TODO: 이후 공지 등이 추가 되었을 때 넣음

    def url(self):
        for anchor  in self.soup.select("ul.ntcList > li > a"):
            # 테스트
            print(BASE + anchor.get("href"))

            # TODO: DB에 넣는 처리

    def image(self):
        for anchor in self.soup.select("ul.ntcList > li > a > img"):
            img_url = BASE + anchor.get("src")
            img_name = img_url[img_url.rfind('/')+1:]

            #print(EVENT_DIRECTORY)
            urllib.request.urlretrieve(img_url, EVENT_DIRECTORY + img_name)

    def title(self):
        for anchor in self.soup.select("ul.ntcList > li > a > dl > dt"):
            print(anchor.get_text())

    def date(self):
        for anchor in self.soup.select("ul.ntcList > li > a > dl > dd:nth-child(3)"):
            print(anchor.get_text())