from csp.abc.herustic.value import ValueHeuristic
from csp.abc.value import TValue
from csp.abc.variable import Variable


class LeastConstrainingValues(ValueHeuristic[TValue]):
    def get_sorted_values(
        self,
        variable: Variable[TValue],
    ) -> list[TValue]:
        return sorted(
            variable.get_available_values(),
            key=lambda value: self._number_of_available_values(variable, value),
            reverse=True,
        )

    @staticmethod
    def _number_of_available_values(
        variable: Variable[TValue],
        value: TValue,
    ) -> int:
        variable.try_value(value)

        constrained_variables = set(
            constrained_variable
            for constraint in variable.get_constraints()
            for constrained_variable in constraint.get_variables()
        )
        constrained_variables.remove(variable)

        number_of_available_values = 0
        for constrained_variable in constrained_variables:
            if constrained_variable.value is None:
                for constrained_value in constrained_variable.get_available_values():
                    if constrained_variable.try_value(constrained_value):
                        number_of_available_values += 1
                constrained_variable.reset()

        variable.reset()

        return number_of_available_values
