import itertools

from csp.abc.constraint import Constraint
from csp.abc.variable import Variable


class IsSkyscrapperRule(Constraint[int]):
    def __init__(
        self,
        variables: list[Variable[int]],
        number: int,
    ) -> None:
        self._variables = variables
        self._number = number

        self._count_combinations()

        for variable in self._variables:
            variable.add_constraint(self)

    def __bool__(self) -> bool:
        values = tuple(variable.value for variable in self._variables)
        return values in self._combinations

    @staticmethod
    def _count(
        values: tuple[int, ...],
    ) -> int:
        number = 0
        max_value = 0
        for value in values:
            if max_value < value:
                max_value = value
                number += 1
        return number

    def _count_combinations(self) -> None:
        self._combinations = set()
        for values in itertools.permutations(range(1, len(self._variables) + 1)):
            if self._count(values) == self._number:
                self._combinations.update(self._get_combinations_with_mask(values))

    def _get_combinations_with_mask(
        self,
        values: tuple[int, ...],
    ) -> list[tuple[int | None, ...]]:
        if len(values) == 0:
            return [tuple()]

        combinations = []
        for combination in self._get_combinations_with_mask(values[1:]):
            combinations.append((values[0], *combination))
            combinations.append((None, *combination))

        return combinations

    def get_variables(self) -> list[Variable[int]]:
        return self._variables.copy()
