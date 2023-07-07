from collections import defaultdict
from pathlib import Path

from csp.abc.model import Model
from csp.abc.variable import Variable
from csp.constraints.skyscrapper import IsSkyscrapperRule
from csp.constraints.unique import IsUnique


class Skyscrapper(Model[int]):
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

        self.top = []
        self.bottom = []
        self.left = []
        self.right = []

        for row, line in enumerate(lines[1:5]):
            label, *values = line.split(";")
            for col, value in enumerate(values):
                match label:
                    case "G":
                        self.top.append(int(value))
                    case "D":
                        self.bottom.append(int(value))
                    case "L":
                        self.left.append(int(value))
                    case "P":
                        self.right.append(int(value))

        rows: dict[int, list[Variable[int]]] = defaultdict(list)
        cols: dict[int, list[Variable[int]]] = defaultdict(list)

        for row in range(self.board_size):
            for col in range(self.board_size):
                variable = Variable(
                    domain=domain,
                )
                self.add_variable(variable)
                rows[row].append(variable)
                cols[col].append(variable)

        for variables in rows.values():
            self.add_constraint(IsUnique(variables))

        for variables in cols.values():
            self.add_constraint(IsUnique(variables))

        for i, number in enumerate(self.top):
            if number:
                self.add_constraint(IsSkyscrapperRule(cols[i], number))

        for i, number in enumerate(self.bottom):
            if number:
                self.add_constraint(IsSkyscrapperRule(cols[i][::-1], number))

        for i, number in enumerate(self.left):
            if number:
                self.add_constraint(IsSkyscrapperRule(rows[i], number))

        for i, number in enumerate(self.right):
            if number:
                self.add_constraint(IsSkyscrapperRule(rows[i][::-1], number))

    def __str__(self) -> str:
        board = "    "
        board += " ".join(f"_{value}_" for value in self.top)
        board += "\n"

        variables = self.get_variables(return_constants=True)
        for i in range(self.board_size):
            board += f" {self.left[i]} "
            for j in range(self.board_size):
                value = variables[i * self.board_size + j].value
                if value is None:
                    if i + 1 == self.board_size:
                        board += "|___"
                    else:
                        board += "|   "
                else:
                    if i + 1 == self.board_size:
                        board += f"|_{value}_"
                    else:
                        board += f"| {value} "
            board += f"| {self.right[i]} \n"

        board += "    "
        board += " ".join(f" {value} " for value in self.bottom)
        board += "\n"

        return board
