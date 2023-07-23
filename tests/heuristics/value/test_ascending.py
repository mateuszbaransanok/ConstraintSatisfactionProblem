from unittest import TestCase
from unittest.mock import Mock

from csp.abc.heuristics.value import ValueHeuristic
from csp.heuristics.value.ascending import AscendingValues


class TestAscendingValues(TestCase):
    def test(self) -> None:
        variable = Mock(get_available_values=Mock(return_value=[2, 4, 1, 3]))
        expected = [1, 2, 3, 4]
        heuristic: ValueHeuristic[int] = AscendingValues()

        actual = heuristic.get_sorted_values(variable)

        self.assertEqual(expected, actual)
