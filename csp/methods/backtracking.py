from csp.abc.method import Method
from csp.abc.value import TValue
from csp.abc.variable import Variable


class Backtracking(Method[TValue]):
    def algorithm(
        self,
        variables: list[Variable[TValue]],
    ) -> bool:
        if not variables:
            self.add_solution()
            return True

        variable, *variables = self.variable_heuristic.get_sorted_variables(variables)

        for value in self.value_heuristic.get_sorted_values(variable):
            self.iterations += 1
            if (
                variable.try_value(value)
                and self.algorithm(variables)
                and not self.find_all_solutions
            ):
                return True

        self.backtracks += 1
        variable.reset()

        return False
