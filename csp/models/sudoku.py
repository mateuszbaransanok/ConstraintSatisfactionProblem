from pathlib import Path

from csp.abc.model import Model
from csp.abc.variable import Variable
from csp.constraints.unique import IsUnique


class Sudoku(Model[int]):
    def __init__(
        self,
        path: Path,
    ) -> None:
        super().__init__(
            name=path.name,
        )
        board = path.read_text().splitlines()[0]
        domain = list(range(1, 10))

        for value in board:
            if value == ".":
                variable = Variable(
                    domain=domain,
                )
            else:
                variable = Variable(
                    value=int(value),
                )
            self.add_variable(variable)

        for i in range(9):
            self.add_constraint(IsUnique(self._variables[i * 9 : i * 9 + 9]))
            self.add_constraint(IsUnique(self._variables[i::9]))
            row, col = divmod(i, 3)
            start = row * 27 + 3 * col
            self.add_constraint(
                IsUnique(
                    self._variables[start : start + 3]
                    + self._variables[9 + start : 9 + start + 3]
                    + self._variables[18 + start : 18 + start + 3]
                )
            )

    def __str__(self) -> str:
        board = " _____________________________ \n"

        variables = self.get_variables(return_constants=True)
        for i in range(9):
            for j in range(9):
                if j % 3 == 0:
                    board += "|"

                value = variables[i * 9 + j].value

                if i % 3 == 2:
                    if value is None:
                        board += "___"
                    else:
                        board += f"_{value}_"
                else:
                    if value is None:
                        board += "   "
                    else:
                        board += f" {value} "

            board += "|\n"

        return board
