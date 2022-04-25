import unittest
from unittest import mock
from unittest.mock import patch
from main import Game
from classes import *

class TestGame(unittest.TestCase):
    def test_person_init(self):
        p = Person()
        self.assertEqual(p.bank, 500)
        self.assertEqual(p.current_bet, 0)
        self.assertEqual(p.num_choice, 40)
        self.assertEqual(p.choice, '')
        self.assertEqual(p.odds, 0)
    
    @patch('classes.Person.get_input')
    def test_input_helper(self,input_mock):
        input_mock.return_value = 'test'
        p = Person()
        self.assertEqual(p.get_input(), 'test')

    def test_roulette_init(self):
        r = Roulette()
        self.assertEqual(len(r.numbers),37)
        self.assertEqual(len(r.colors),37)
        self.assertEqual(r.number,0)
        self.assertEqual(r.min,1)
        self.assertEqual(r.max,1000)
        self.assertEqual(r.color,'')
        self.assertEqual(r.dozen,'')
        self.assertEqual(r.even_odd,'')
        self.assertEqual(r.low_high,'')


if __name__ == '__main__':
    unittest.main()