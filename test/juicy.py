# 쥬씨 크롤링
# 이벤트
#   - 이벤트 세부 페이지 url
#   - 이미지
#   - 제목
#   - 등록일
# "http://www.no1juicy.com/bbs/board/lists/2?bo_table=event"
# http://www.no1juicy.com/bbs/board/view?bo_table=event&wr_id=82


from bs4 import BeautifulSoup
from urllib.request import urlopen

BASE = "http://www.no1juicy.com"
EVENT = "http://www.no1juicy.com/bbs/board/lists?bo_table=event"

class Juicy:
    def crawling(self):
        self.url()

        # TODO: 이후 공지 등이 추가 되었을 때 넣음

    def url(self):
        response = urlopen(EVENT)
        soup = BeautifulSoup(response, "html.parser")

        for anchor  in soup.select("ul.ntcList > li > a"):
            # 테스트
            print(BASE + anchor.get("href"))

            # TODO: DB에 넣는 처리