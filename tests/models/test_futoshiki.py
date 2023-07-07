from unittest import TestCase

from csp import PROJECT_DIR
from csp.models.futoshiki import Futoshiki


class TestFutoshiki(TestCase):
    def test(self) -> None:
        expected = (
            "    _1_ _2_ _3_ _4_\n"
            " A | 0 | 0 | 0 | 3 |\n"
            " B | 0 | 1 | 0 | 0 |\n"
            " C | 2 | 0 | 0 | 0 |\n"
            " D | 4 | 0 | 0 | 0 |\n"
        )

        actual = str(Futoshiki(PROJECT_DIR / "data/futoshiki/futoshiki_4_0.txt"))

        self.assertEqual(expected, actual)
