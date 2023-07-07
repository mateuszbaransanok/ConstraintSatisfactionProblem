from unittest import TestCase

from csp.abc.variable import Variable
from csp.constraints.lower import IsLower
from csp.constraints.unique import IsUnique
from csp.heuristics.variable.most_constraining import MostConstrainingVariables


class TestMostConstrainingVariables(TestCase):
    def test(self) -> None:
        variable1 = Variable(domain=[1, 2, 3])
        variable2 = Variable(domain=[1, 2, 3])
        variable3 = Variable(domain=[1, 2, 3])
        IsLower(variable2, variable1)
        IsLower(variable2, variable3)
        IsUnique([variable2, variable1])
        variables = [variable1, variable2, variable3]
        expected = [variable2, variable1, variable3]
        heuristic = MostConstrainingVariables()

        actual = heuristic.get_sorted_variables(variables)

        self.assertEqual(expected, actual)
