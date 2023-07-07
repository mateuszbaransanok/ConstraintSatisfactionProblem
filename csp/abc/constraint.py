import typing
from abc import ABC, abstractmethod

from csp.abc.value import TValue

if typing.TYPE_CHECKING:
    from csp.abc.variable import Variable


class Constraint(typing.Generic[TValue], ABC):
    @abstractmethod
    def __bool__(self) -> bool:
        pass

    @abstractmethod
    def get_variables(self) -> list["Variable[TValue]"]:
        pass
