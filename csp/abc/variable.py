from typing import Generic

from csp.abc.constraint import Constraint
from csp.abc.value import TValue


class Variable(Generic[TValue]):
    def __init__(
        self,
        value: TValue | None = None,
        domain: list[TValue] | None = None,
    ) -> None:
        if not ((value is None) ^ (domain is None)):
            raise ValueError("Should be provided only value or only domain")

        self._value: TValue | None = value
        self._domain: list[TValue]
        self._available_values: list[TValue]
        self._is_constant: bool

        if domain is None:
            self._domain = [value]  # type: ignore[list-item]
            self._available_values = []
            self._is_constant = True
        else:
            self._domain = domain
            self._available_values = domain.copy()
            self._is_constant = False

        self._constraints: list[Constraint[TValue]] = []

    def __repr__(self) -> str:
        return f"Variable({self._value})"

    def add_constraint(
        self,
        constraint: Constraint[TValue],
    ) -> None:
        self._constraints.append(constraint)

    def get_constraints(self) -> list[Constraint[TValue]]:
        return self._constraints.copy()

    def get_domain(self) -> list[TValue]:
        return self._domain.copy()

    def get_available_values(self) -> list[TValue]:
        return self._available_values.copy()

    @property
    def value(self) -> TValue | None:
        return self._value

    @property
    def is_constant(self) -> bool:
        return self._is_constant

    def try_value(
        self,
        value: TValue,
    ) -> bool:
        if value not in self._available_values:
            raise ValueError("Values outside the available values cannot be tried")
        self._value = value
        self._available_values.remove(value)
        return all(self._constraints)

    def reset(self) -> None:
        self._value = None
        self._available_values = self._domain.copy()
