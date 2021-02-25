# RPORT

# 1. 이벤트
## 1.1. 이벤트 페이지 크롤링 실패
이벤트 페이지가 html 형식으로 이루어진 것이 아닌 javascript 형식으로 이루어저있어 beautifulsoup로 크롤링할 수 없었음

* 스타벅스 - 페이지 전체가 자바스크립트로 구성되어 있음
* 투썸플레이스 - 링크가 자바스크립트로 구성되어 있음
* 엔제리너스 - 링크가 자바스크립트로 구성되어 있음
* 할리스 - 링크가 자바스크립트로 구성되어 있음

## 1.2. 이벤트 기간 표시 태그영역의 유무
이벤트 기간을 표시할 때, 이벤트 기간이 명시되어 있을 때는 ```<p class="date">``` 태그가 존재하지만 이벤트 기간이 명시되어 있지 안을 때는 ```<p class="date">``` 태그가 존재하지 안는다.
이는 크롤링을 시도할 때, 태그가 존재하지 않아 ""으로도 정보를 저장할 수 없어 다른 이벤트 정보를 저장하는 인덱스와 이벤트 기간 리스트의 인덱스에 차이가 생겨 알맞은 쌍의 정보를 DB에 저장할 수 없다.

* 공차

## 1.3. primary key 설정
DB에 primary key를 설정해야 하는데 이를 위한 값을 무엇으로 할지가 매우 고민됨

* 투썸플레이스 - 이미지의 특정 수
    * 예)
        * /Twosome_file/TWOSOME_EVENT_BBS/```450```_img03
        * /Twosome_file/TWOSOME_EVENT_BBS/```449```_img03
* 엔제리너스 - 이미지의 특정 수
    * 예)
        * /Data/Event/EventImage```691```.jpg
        * /Data/Event/EventImage```625```.jpg
* 공차
* 할리스 - 이미지의 특정 수
    * 예)
        * newsEvent_```202102220426214180```.jpg
        * newsEvent_```202101290350507760```.jpg
* 주씨 - 링크에 id 명시
    * 예)
        * /bbs/board/view?bo_table=event&wr_id=```82```
        * /bbs/board/view?bo_table=event&wr_id=```81```
* 메가커피 - 게시판 번호
* 빽다방 - 게시판 번호
* 스타벅스 - 페이지 분석 실패
* 탐앤탐스 - 링크에 id 명시
    * 예)
        * /event/event.html?bmain=view&uid=```27```&mode=
        * /event/event.html?bmain=view&uid=```28```&mode=