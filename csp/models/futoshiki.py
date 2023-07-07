from collections import defaultdict
from pathlib import Path

from csp.abc.model import Model
from csp.abc.variable import Variable
from csp.constraints.lower import IsLower
from csp.constraints.unique import IsUnique


class Futoshiki(Model[int]):
    ROW_LABELS = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
    COL_LABELS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def __init__(
        self,
        path: Path,
    ) -> None:
        super().__init__(
            name=path.name,
        )
        lines = path.read_text().splitlines()
        self.board_size = int(lines[0])
        domain = list(range(1, self.board_size + 1))

        named_variables: dict[str, Variable[int]] = {}
        unique_variables: dict[str, list[Variable[int]]] = defaultdict(list)

        for row, line in enumerate(lines[2 : 2 + self.board_size]):
            for col, value in enumerate(line.split(";")):
                if value == "0":
                    variable = Variable(
                        domain=domain,
                    )
                else:
                    variable = Variable(
                        value=int(value),
                    )

                self.add_variable(variable)

                row_name = self.ROW_LABELS[row]
                col_name = self.COL_LABELS[col]

                named_variables[f"{row_name}{col_name}"] = variable
                unique_variables[row_name].append(variable)
                unique_variables[col_name].append(variable)

        for line in lines[3 + self.board_size :]:
            left_name, _, right_name = line.partition(";")

            left_variable = named_variables[left_name]
            right_variable = named_variables[right_name]

            self.add_constraint(IsLower(left_variable, right_variable))

        for variables in unique_variables.values():
            self.add_constraint(IsUnique(variables))

    def __str__(self) -> str:
        board = "    "
        board += " ".join(f"_{col}_" for col in self.COL_LABELS[: self.board_size])
        board += "\n"

        variables = self.get_variables(return_constants=True)
        for i in range(self.board_size):
            board += f" {self.ROW_LABELS[i]} "
            for j in range(self.board_size):
                value = variables[i * self.board_size + j].value
                if value is None:
                    board += "| 0 "
                else:
                    board += f"| {value} "
            board += "|\n"

        return board
