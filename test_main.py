import unittest
from main import Game
from classes import *

class TestGame(unittest.TestCase):
    def test_person_init(self):
        p = Person()
        self.assertEquals(p.bank, 500)
        self.assertEquals(p.current_bet, 0)
        self.assertEquals(p.num_choice, 40)
        self.assertEquals(p.choice, '')
        self.assertEquals(p.odds, 0)

    def test_roulette_init(self):
        r = Roulette()
        self.assertEquals(len(r.numbers),37)
        self.assertEquals(len(r.colors),37)
        self.assertEquals(r.number,0)
        self.assertEquals(r.min,1)
        self.assertEquals(r.max,1000)
        self.assertEquals(r.color,'')
        self.assertEquals(r.dozen,'')
        self.assertEquals(r.even_odd,'')
        self.assertEquals(r.low_high,'')


if __name__ == '__main__':
    unittest.main()