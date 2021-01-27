# 스타벅스 크롤링
# 이벤트
#   - 이벤트 세부 페이지 url
#   - 이미지
#   - 제목
#   - 기간

from selenium import webdriver

from bs4 import BeautifulSoup
from urllib.request import urlopen

def test():
    DRIVER_PATH = "C:/tools/chromedriver.exe"
    starbucks_event = "https://www.starbucks.co.kr/whats_new/campaign_list.do"

    driver = webdriver.Chrome(DRIVER_PATH)
    driver.get(starbucks_event)

    print(driver.find_element_by_class_name("goPromotionView"))

class Event:
    def crawling(self):
        print("test")