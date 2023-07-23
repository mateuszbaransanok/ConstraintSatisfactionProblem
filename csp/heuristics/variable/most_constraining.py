from csp.abc.heuristics.variable import VariableHeuristic
from csp.abc.value import TValue
from csp.abc.variable import Variable


class MostConstrainingVariables(VariableHeuristic[TValue]):
    def get_sorted_variables(
        self,
        variables: list[Variable[TValue]],
    ) -> list[Variable[TValue]]:
        return sorted(variables, key=self._number_of_constrained_variables, reverse=True)

    @staticmethod
    def _number_of_constrained_variables(
        variable: Variable[TValue],
    ) -> int:
        return sum(1 for const in variable.get_constraints() for _ in const.get_variables()[1:])
