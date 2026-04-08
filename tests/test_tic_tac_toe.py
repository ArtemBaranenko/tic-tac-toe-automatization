import unittest
from src import tic_tac_toe

class TestTicTac(unittest.TestCase):

    def test_check_rows(self):
        board=[["X", "X", "X"],[" ", " ", " "],[" ", " ", " "]]
        self.assertTrue(tic_tac_toe.is_win("X",board))

    def test_check_columns(self):
        board=[["O", "X", "X"],["O", " ", " "],["O", "X", " "]]
        self.assertTrue(tic_tac_toe.is_win("O",board))

    def test_check_diagonals(self):
        board=[["X", "O", " "],[" ", "X", " "],[" ", "O", "X"]]
        self.assertTrue(tic_tac_toe.is_win("X",board))
        board = [[" ", "O", "X"], [" ", "X", " "], ["X", "O", " "]]
        self.assertTrue(tic_tac_toe.is_win("X", board))