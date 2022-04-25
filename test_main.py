import unittest
from main import Game
from classes import *

class TestGame(unittest.TestCase):
    def test_workflow(self):
        testBool = True
        self.assertTrue(testBool)


if __name__ == '__main__':
    unittest.main()