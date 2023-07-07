from dataclasses import dataclass
from typing import Generic

from csp.abc.model import Model
from csp.abc.value import TValue


@dataclass
class Solution(Generic[TValue]):
    model: Model[TValue]
    iterations: int
    backtracks: int
    time: float
