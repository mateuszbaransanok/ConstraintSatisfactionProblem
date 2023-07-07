from csp.abc.method import Method
from csp.abc.value import TValue
from csp.abc.variable import Variable


class ForwardChecking(Method[TValue]):
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
                and self._validate_constrained_variables(variable)
                and self.algorithm(variables)
                and not self.find_all_solutions
            ):
                return True

        self.backtracks += 1
        variable.reset()

        return False

    def _validate_constrained_variables(
        self,
        variable: Variable[TValue],
    ) -> bool:
        constrained_variables = set()
        for constraint in variable.get_constraints():
            constrained_variables.update(constraint.get_variables())

        constrained_variables.remove(variable)

        for constrained_variable in constrained_variables:
            if constrained_variable.value is None and not self._validate_domain_values(
                constrained_variable
            ):
                return False

        return True

    @staticmethod
    def _validate_domain_values(
        variable: Variable[TValue],
    ) -> bool:
        for value in variable.get_available_values():
            if variable.try_value(value):
                variable.reset()
                return True

        variable.reset()
        return False
