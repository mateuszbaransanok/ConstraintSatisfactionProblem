from csp.abc.herustic.variable import VariableHeuristic
from csp.abc.value import TValue
from csp.abc.variable import Variable


class InOrderVariables(VariableHeuristic[TValue]):
    def get_sorted_variables(
        self,
        variables: list[Variable[TValue]],
    ) -> list[Variable[TValue]]:
        return variables
