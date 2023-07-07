from abc import ABC, abstractmethod
from typing import Generic

from csp.abc.value import TValue
from csp.abc.variable import Variable


class ValueHeuristic(Generic[TValue], ABC):
    @abstractmethod
    def get_sorted_values(
        self,
        variable: Variable[TValue],
    ) -> list[TValue]:
        pass
