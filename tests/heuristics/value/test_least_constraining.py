from unittest import TestCase

from csp.abc.variable import Variable
from csp.constraints.unique import IsUnique
from csp.heuristics.value.least_constraining import LeastConstrainingValues


class TestLeastConstrainingValues(TestCase):
    def test(self) -> None:
        variable = Variable(domain=[1, 2, 3])
        IsUnique([variable, Variable(domain=[1, 3]), Variable(domain=[3])])
        expected = [2, 1, 3]
        heuristic = LeastConstrainingValues()

        actual = heuristic.get_sorted_values(variable)

        self.assertEqual(expected, actual)
