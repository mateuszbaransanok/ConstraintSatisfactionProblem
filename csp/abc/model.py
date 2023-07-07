from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Generic

from csp.abc.constraint import Constraint
from csp.abc.value import TValue
from csp.abc.variable import Variable


class Model(Generic[TValue], ABC):
    def __init__(
        self,
        name: str,
    ) -> None:
        self._name = name
        self._variables: list[Variable[TValue]] = []
        self._constraints: list[Constraint[TValue]] = []

    @property
    def name(self) -> str:
        return self._name

    def add_variable(
        self,
        variable: Variable[TValue],
    ) -> None:
        self._variables.append(variable)

    def add_constraint(
        self,
        constraint: Constraint[TValue],
    ) -> None:
        self._constraints.append(constraint)

    def get_variables(
        self,
        return_constants: bool = False,
    ) -> list[Variable[TValue]]:
        return [
            variable for variable in self._variables if return_constants or not variable.is_constant
        ]

    def get_constraints(self) -> list[Constraint[TValue]]:
        return self._constraints.copy()

    def copy(self) -> "Model[TValue]":
        return deepcopy(self)

    @abstractmethod
    def __str__(self) -> str:
        pass
