from unittest import TestCase

from csp import PROJECT_DIR
from csp.methods.backtracking import Backtracking
from csp.models.futoshiki import Futoshiki


class TestBacktracking(TestCase):
    def test__futoshiki(self) -> None:
        method = Backtracking(
            model=Futoshiki(PROJECT_DIR / "data/futoshiki/futoshiki_4_0.txt"),
        )
        expected_model = (
            "    _1_ _2_ _3_ _4_\n"
            " A | 1 | 4 | 2 | 3 |\n"
            " B | 3 | 1 | 4 | 2 |\n"
            " C | 2 | 3 | 1 | 4 |\n"
            " D | 4 | 2 | 3 | 1 |\n"
        )
        expected_iterations = 82
        expected_backtracks = 13

        method.start()

        self.assertEqual(expected_model, str(method.model))
        self.assertEqual(expected_iterations, method.iterations)
        self.assertEqual(expected_backtracks, method.backtracks)
