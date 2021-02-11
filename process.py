import cafe.juicy.juicy as juciy
import cafe.gong_cha.gong_cha as gong_cha
import cafe.paikdabang.paikdabang as paikdabang
import cafe.mega_coffee.mega_coffee as mega_coffee
import cafe.hollys.hollys as hollys
import cafe.angel_in_us.angel_in_us as angel_in_us
import cafe.tom_n_toms.tom_n_toms as tom_n_toms
import cafe.a_twosome_place.a_twosome_place as a_twosome_place

def run():
    juciy.crawling()
    gong_cha.crawling()
    paikdabang.crawling()
    mega_coffee.crawling()
    hollys.crawling()       # url 크롤링 실패
    angel_in_us.crawling()  # url 크롤링 실패
    tom_n_toms.crawling()
    a_twosome_place.crawling()