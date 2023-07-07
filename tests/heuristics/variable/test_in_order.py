from unittest import TestCase
from unittest.mock import Mock

from csp.heuristics.variable.in_order import InOrderVariables


class TestInOrderVariables(TestCase):
    def test(self) -> None:
        variables = [Mock(), Mock(), Mock()]
        expected = variables.copy()
        heuristic = InOrderVariables()

        actual = heuristic.get_sorted_variables(variables)

        self.assertEqual(expected, actual)
