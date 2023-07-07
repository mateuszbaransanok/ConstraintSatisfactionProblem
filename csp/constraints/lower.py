from csp.abc.constraint import Constraint
from csp.abc.variable import Variable


class IsLower(Constraint[int]):
    def __init__(
        self,
        lower: Variable[int],
        greater: Variable[int],
    ) -> None:
        self._lower = lower
        self._greater = greater

        self._lower.add_constraint(self)
        self._greater.add_constraint(self)

    def __bool__(self) -> bool:
        return (
            self._lower.value is None
            or self._greater.value is None
            or self._lower.value < self._greater.value
        )

    def get_variables(self) -> list[Variable[int]]:
        return [self._lower, self._greater]
