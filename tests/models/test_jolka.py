from unittest import TestCase

from csp import PROJECT_DIR
from csp.models.jolka import Jolka


class TestJolka(TestCase):
    def test(self) -> None:
        expected = "____\n___#\n____\n"

        actual = str(Jolka(PROJECT_DIR / "data/jolka/jolka_0.txt"))

        self.assertEqual(expected, actual)
