from cafe.juicy.juicy import Juicy
from cafe.mega_coffee.mega_coffee import Mega_Coffee
from cafe.paikdabang.paikdabang import Paikdabang

class Process:
    def __init__(self):
        self.juciy = Juicy()
        self.mega_coffee = Mega_Coffee()
        self.paikdabang = Paikdabang()

    def run(self):
        self.juciy.crawling()
        self.mega_coffee.crawling()
        self.paikdabang.crawling()