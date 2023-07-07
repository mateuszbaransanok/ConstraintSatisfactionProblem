from csp.abc.constraint import Constraint
from csp.abc.variable import Variable


class IsJolkaRule(Constraint[str]):
    def __init__(
        self,
        h_variable: Variable[str],
        h_index: int,
        v_variable: Variable[str],
        v_index: int,
    ) -> None:
        self._h_variable = h_variable
        self._h_index = h_index
        self._v_variable = v_variable
        self._v_index = v_index

        self._h_variable.add_constraint(self)
        self._v_variable.add_constraint(self)

    def __bool__(self) -> bool:
        return (
            self._h_variable.value is None
            or self._v_variable.value is None
            or self._h_variable.value[self._h_index] == self._v_variable.value[self._v_index]
        )

    def get_variables(self) -> list[Variable[str]]:
        return [self._h_variable, self._v_variable]
