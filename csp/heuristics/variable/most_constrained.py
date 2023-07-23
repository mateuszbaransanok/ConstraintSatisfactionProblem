from csp.abc.heuristics.variable import VariableHeuristic
from csp.abc.value import TValue
from csp.abc.variable import Variable


class MostConstrainedVariables(VariableHeuristic[TValue]):
    def get_sorted_variables(
        self,
        variables: list[Variable[TValue]],
    ) -> list[Variable[TValue]]:
        return sorted(variables, key=self._number_of_available_values)

    @staticmethod
    def _number_of_available_values(
        variable: Variable[TValue],
    ) -> int:
        count = sum(variable.try_value(value) for value in variable.get_available_values())
        variable.reset()
        return count
