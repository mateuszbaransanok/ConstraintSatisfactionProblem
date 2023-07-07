from unittest import TestCase

from csp import PROJECT_DIR
from csp.models.sudoku import Sudoku


class TestSudoku(TestCase):
    def test(self) -> None:
        expected = (
            " _____________________________ \n"
            "| 6  2  5 |       1 |       8 |\n"
            "|    7    |    8    |       6 |\n"
            "|_8_______|_________|_________|\n"
            "| 2       |       4 |         |\n"
            "|    4    |    1    | 3       |\n"
            "|_________|_________|_1_______|\n"
            "|         |       7 |    3  2 |\n"
            "|         |       6 |    9    |\n"
            "|____8__4_|____3____|_________|\n"
        )

        actual = str(Sudoku(PROJECT_DIR / "data/sudoku/sudoku_0_0.txt"))

        self.assertEqual(expected, actual)
