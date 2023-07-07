from random import shuffle

from csp.abc.herustic.value import ValueHeuristic
from csp.abc.value import TValue
from csp.abc.variable import Variable


class RandomValues(ValueHeuristic[TValue]):
    def get_sorted_values(
        self,
        variable: Variable[TValue],
    ) -> list[TValue]:
        values = variable.get_available_values()
        shuffle(values)
        return values
