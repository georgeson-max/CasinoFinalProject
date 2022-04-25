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

    @patch('classes.Person.get_input')
    def test_make_choice(self, input_mock):          #integration test 
        p = Person()
        r = Roulette()
        input_mock.return_value = 2
        self.assertEqual(r.make_choice(p),2)

    @patch('classes.Person.get_input')
    def test_bet_even(self, input_mock):             #integration test 
        p = Person()
        r = Roulette()
        input_mock.return_value = 1
        self.assertTrue(r.bet_even(p))
        self.assertEqual(p.odds, 1)
        self.assertEqual(p.choice,'red')

        input_mock.return_value = 2
        self.assertTrue(r.bet_even(p))
        self.assertEqual(p.odds, 1)
        self.assertEqual(p.choice,'black')

        input_mock.return_value = 3
        self.assertTrue(r.bet_even(p))
        self.assertEqual(p.odds, 1)
        self.assertEqual(p.choice,'Even')

        input_mock.return_value = 4
        self.assertTrue(r.bet_even(p))
        self.assertEqual(p.odds, 1)
        self.assertEqual(p.choice,'Odd')

        input_mock.return_value = 5
        self.assertTrue(r.bet_even(p))
        self.assertEqual(p.odds, 1)
        self.assertEqual(p.choice,'Low')

        input_mock.return_value = 6
        self.assertTrue(r.bet_even(p))
        self.assertEqual(p.odds, 1)
        self.assertEqual(p.choice,'High')

        input_mock.return_value = 0
        self.assertFalse(r.bet_even(p))


    @patch('classes.Person.get_input')
    def test_bet_dozen(self, input_mock):            #integration test 
        p = Person()
        r = Roulette()
        input_mock.return_value = 1
        self.assertTrue(r.bet_dozen(p))
        self.assertEqual(p.odds, 2)
        self.assertEqual(p.choice,'first')

        input_mock.return_value = 2
        self.assertTrue(r.bet_dozen(p))
        self.assertEqual(p.odds, 2)
        self.assertEqual(p.choice,'second')

        input_mock.return_value = 3
        self.assertTrue(r.bet_dozen(p))
        self.assertEqual(p.odds, 2)
        self.assertEqual(p.choice,'third')

        input_mock.return_value = 0
        self.assertFalse(r.bet_dozen(p))

    @patch('classes.Person.get_input')
    def test_bet_straight(self, input_mock):         #integration test 
        p = Person()
        r = Roulette()
        input_mock.return_value = 1
        self.assertTrue(r.bet_straight(p))
        self.assertEqual(p.odds, 35)
        self.assertEqual(p.num_choice, 1)

        input_mock.return_value = 36
        self.assertTrue(r.bet_straight(p))
        self.assertEqual(p.odds, 35)
        self.assertEqual(p.num_choice, 36)

        input_mock.return_value = 0
        self.assertFalse(r.bet_straight(p))

        input_mock.return_value = 'f'
        self.assertFalse(r.bet_straight(p))

    def test_spin(self):
        r = Roulette()
        self.assertTrue(r.spin(1))
        self.assertEqual(r.number, 1)
        self.assertEqual(r.color, 'red')
        self.assertEqual(r.dozen, 'first')
        self.assertEqual(r.even_odd, 'Odd')
        self.assertEqual(r.low_high, 'Low')


        self.assertTrue(r.spin(20))
        self.assertEqual(r.number, 20)
        self.assertEqual(r.color, 'black')
        self.assertEqual(r.dozen, 'second')
        self.assertEqual(r.even_odd, 'Even')
        self.assertEqual(r.low_high, 'High')

        self.assertTrue(r.spin(33))
        self.assertEqual(r.number, 33)
        self.assertEqual(r.color, 'black')
        self.assertEqual(r.dozen, 'third')
        self.assertEqual(r.even_odd, 'Odd')
        self.assertEqual(r.low_high, 'High')

        self.assertFalse(r.spin(0))
        self.assertEqual(r.number, 0)
        self.assertEqual(r.color, 'green')
        self.assertEqual(r.dozen, 'zero')
        self.assertEqual(r.even_odd, 'zero')
        self.assertEqual(r.low_high, 'zero')

    def test_check_winner(self):                     #integration test 
        p = Person()
        r = Roulette()
        p.num_choice = 1
        r.spin(1)
        self.assertTrue(r.check_winner(p))

        p = Person()
        p.choice = 'Odd'
        r.spin(3)
        self.assertTrue(r.check_winner(p))

        p = Person()
        p.choice = 'red'
        r.spin(12)
        self.assertTrue(r.check_winner(p))

        p = Person()
        p.choice = 'first'
        r.spin(2)
        self.assertTrue(r.check_winner(p))

        p = Person()
        p.choice = 'Low'
        r.spin(4)
        self.assertTrue(r.check_winner(p))

        p = Person()
        p.num_choice = 1
        r.spin(2)
        self.assertFalse(r.check_winner(p))

        p = Person()
        p.choice = 'Odd'
        r.spin(4)
        self.assertFalse(r.check_winner(p))

        p = Person()
        p.choice = 'red'
        r.spin(13)
        self.assertFalse(r.check_winner(p))

        p = Person()
        p.choice = 'first'
        r.spin(15)
        self.assertFalse(r.check_winner(p))

        p = Person()
        p.choice = 'Low'
        r.spin(20)
        self.assertFalse(r.check_winner(p))

        p = Person()
        p.choice = 'Low'
        r.spin(0)
        self.assertFalse(r.check_winner(p))

    def test_payout(self):                           #integration test
        r = Roulette()
        p = Person()
        p.current_bet = 50
        p.bank = 450
        p.odds = 1
        r.payout(p)
        self.assertEqual(p.bank, 550)
        self.assertEqual(p.current_bet, 0)

        p = Person()
        p.current_bet = 50
        p.bank = 450
        p.odds = 2
        r.payout(p)
        self.assertEqual(p.bank, 600)
        self.assertEqual(p.current_bet, 0)

        p = Person()
        p.current_bet = 1
        p.bank = 499
        p.odds = 35
        r.payout(p)
        self.assertEqual(p.bank, 535)
        self.assertEqual(p.current_bet, 0)

    @patch('classes.Person.get_input')
    def test_make_bet(self, input_mock):             #integration test
        r = Roulette()
        p = Person()
        input_mock.return_value = 0
        self.assertFalse(r.make_bet(p))
        self.assertEqual(p.bank,500)
        self.assertEqual(p.current_bet, 0)

        input_mock.return_value = 550
        self.assertFalse(r.make_bet(p))
        self.assertEqual(p.bank,500)
        self.assertEqual(p.current_bet, 0)

        input_mock.return_value = 1050
        self.assertFalse(r.make_bet(p))
        self.assertEqual(p.bank,500)
        self.assertEqual(p.current_bet, 0)

        input_mock.return_value = -1
        self.assertFalse(r.make_bet(p))
        self.assertEqual(p.bank,500)
        self.assertEqual(p.current_bet, 0)

        input_mock.return_value = 'f'
        self.assertFalse(r.make_bet(p))
        self.assertEqual(p.bank,500)
        self.assertEqual(p.current_bet, 0)

        input_mock.return_value = 50
        self.assertTrue(r.make_bet(p))
        self.assertEqual(p.bank,450)
        self.assertEqual(p.current_bet, 50)

        input_mock.return_value = 550
        p.bank = 550
        self.assertTrue(r.make_bet(p))
        self.assertEqual(p.bank,0)
        self.assertEqual(p.current_bet, 550)

    @patch('classes.Person.get_input')
    def test_play_again(self, input_mock):             #integration test
        r = Roulette()
        p = Person()
        input_mock.return_value = 'y'
        self.assertTrue(r.play_again(p))
        input_mock.return_value = 'Y'
        self.assertTrue(r.play_again(p))

        input_mock.return_value = 'n'
        self.assertFalse(r.play_again(p))
        input_mock.return_value = 'f'
        self.assertFalse(r.play_again(p))
        input_mock.return_value = 0
        self.assertFalse(r.play_again(p))
        input_mock.return_value = -5.6
        self.assertFalse(r.play_again(p))

        p.bank = 0
        input_mock.return_value = 'y'
        self.assertFalse(r.play_again(p))



if __name__ == '__main__':
    unittest.main()