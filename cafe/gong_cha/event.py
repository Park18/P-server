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

import os # 실행 위치

from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request

from dir_manager import create_file

BASE = "http://www.gong-cha.co.kr"
EVENT = "http://www.gong-cha.co.kr/brand/board/event.php?status=ing"

EVENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__)) + '/event/'

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
        for anchor  in self.soup.select("div.imgs > a"):
            # 테스트
            print(anchor.get("href"))

            # TODO: DB push

    def image(self):
        for anchor in self.soup.select("div.imgs > a > img"):
            img_url = BASE + anchor.get("src")
            img_name = img_url[img_url.rfind('/')+1:]

            # 이미지를 다운 받거나 img_url Db push
            create_file(img_url, EVENT_DIRECTORY, img_name)

    def title(self):
        for anchor in self.soup.select("p.tit"):
            print(anchor.get_text())

            # TODO: DB push

    def date(self):
        # TODO: 기간이 존재하지 않은 이벤트가 있기 때문에 순서의 오류 발생 가능
        for anchor in self.soup.select("p.date"):
            print(anchor.get_text())

            # TODO: DB push
