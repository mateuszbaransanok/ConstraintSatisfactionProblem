from abc import ABC, abstractmethod
from typing import Generic

from csp.abc.value import TValue
from csp.abc.variable import Variable


class VariableHeuristic(Generic[TValue], ABC):
    @abstractmethod
    def get_sorted_variables(
        self,
        variables: list[Variable[TValue]],
    ) -> list[Variable[TValue]]:
        pass
