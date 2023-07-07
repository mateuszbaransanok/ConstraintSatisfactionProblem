from unittest import TestCase

from csp import PROJECT_DIR
from csp.models.skyscrapper import Skyscrapper


class TestSkyscrapper(TestCase):
    def test(self) -> None:
        expected = (
            "    _2_ _3_ _0_ _1_\n"
            " 0 |   |   |   |   | 0 \n"
            " 0 |   |   |   |   | 2 \n"
            " 3 |   |   |   |   | 0 \n"
            " 0 |___|___|___|___| 0 \n"
            "     0   1   2   4 \n"
        )

        actual = str(Skyscrapper(PROJECT_DIR / "data/skyscrapper/skyscrapper_4_0.txt"))

        self.assertEqual(expected, actual)
