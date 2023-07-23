from unittest import TestCase

from csp.abc.heuristics.variable import VariableHeuristic
from csp.abc.variable import Variable
from csp.heuristics.variable.in_order import InOrderVariables


class TestInOrderVariables(TestCase):
    def test(self) -> None:
        variables = [Variable(value=5), Variable(value=2), Variable(value=3)]
        expected = variables.copy()
        heuristic: VariableHeuristic[int] = InOrderVariables()

        actual = heuristic.get_sorted_variables(variables)

        self.assertEqual(expected, actual)
