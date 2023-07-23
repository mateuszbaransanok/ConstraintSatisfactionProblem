from random import shuffle

from csp.abc.heuristics.variable import VariableHeuristic
from csp.abc.value import TValue
from csp.abc.variable import Variable


class RandomVariables(VariableHeuristic[TValue]):
    def get_sorted_variables(
        self,
        variables: list[Variable[TValue]],
    ) -> list[Variable[TValue]]:
        shuffle(variables)
        return variables
