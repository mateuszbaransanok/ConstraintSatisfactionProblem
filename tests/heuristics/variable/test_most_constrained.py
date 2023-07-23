from unittest import TestCase

from csp.abc.heuristics.variable import VariableHeuristic
from csp.abc.variable import Variable
from csp.heuristics.variable.most_constrained import MostConstrainedVariables


class TestMostConstrainedVariables(TestCase):
    def test(self) -> None:
        variable1 = Variable(domain=[1, 3])
        variable2 = Variable(domain=[2])
        variable3 = Variable(domain=[1, 2, 3])
        variables = [variable1, variable2, variable3]
        expected = [variable2, variable1, variable3]
        heuristic: VariableHeuristic[int] = MostConstrainedVariables()

        actual = heuristic.get_sorted_variables(variables)

        self.assertEqual(expected, actual)
