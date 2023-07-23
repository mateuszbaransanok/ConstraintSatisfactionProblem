from csp.abc.heuristics.value import ValueHeuristic
from csp.abc.value import TValue
from csp.abc.variable import Variable


class AscendingValues(ValueHeuristic[TValue]):
    def get_sorted_values(
        self,
        variable: Variable[TValue],
    ) -> list[TValue]:
        return sorted(variable.get_available_values())  # type: ignore[type-var]
