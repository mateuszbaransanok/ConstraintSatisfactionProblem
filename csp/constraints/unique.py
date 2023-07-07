from typing import Any

from csp.abc.constraint import Constraint
from csp.abc.variable import Variable


class IsUnique(Constraint[Any]):
    def __init__(
        self,
        variables: list[Variable[Any]],
    ) -> None:
        self._variables = variables

        for variable in self._variables:
            variable.add_constraint(self)

    def __bool__(self) -> bool:
        values = [variable.value for variable in self._variables if variable.value is not None]
        return len(values) == len(set(values))

    def get_variables(self) -> list[Variable[Any]]:
        return self._variables.copy()
