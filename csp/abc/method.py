import math
from abc import ABC, abstractmethod
from time import time
from typing import Generic

from csp.abc.heuristics.value import ValueHeuristic
from csp.abc.heuristics.variable import VariableHeuristic
from csp.abc.model import Model
from csp.abc.solution import Solution
from csp.abc.value import TValue
from csp.abc.variable import Variable
from csp.heuristics.value.ascending import AscendingValues
from csp.heuristics.variable.in_order import InOrderVariables


class Method(Generic[TValue], ABC):
    def __init__(
        self,
        model: Model[TValue],
        variable_heuristic: VariableHeuristic[TValue] | None = None,
        value_heuristic: ValueHeuristic[TValue] | None = None,
        find_all_solutions: bool = False,
    ) -> None:
        self.model: Model[TValue] = model
        self.variable_heuristic: VariableHeuristic[TValue] = (
            variable_heuristic or InOrderVariables()
        )
        self.value_heuristic: ValueHeuristic[TValue] = value_heuristic or AscendingValues()
        self.find_all_solutions: bool = find_all_solutions

        self.start_time: float = 0.0
        self.end_time: float = 0.0
        self.iterations: int = 0
        self.backtracks: int = 0
        self.solutions: list[Solution[TValue]] = []

    def total_combinations(self) -> int:
        return math.prod((len(variable.get_domain()) for variable in self.model.get_variables()))

    def add_solution(self) -> None:
        solution = Solution(
            model=self.model.copy(),
            iterations=self.iterations,
            backtracks=self.backtracks,
            time=time() - self.start_time,
        )
        self.solutions.append(solution)

    @abstractmethod
    def algorithm(
        self,
        variables: list[Variable[TValue]],
    ) -> bool:
        pass

    def start(self) -> None:
        variables = self.model.get_variables()
        self.start_time = time()
        self.algorithm(variables)
        self.end_time = time()
