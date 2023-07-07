from pathlib import Path

from csp.abc.model import Model
from csp.abc.variable import Variable
from csp.constraints.jolka import IsJolkaRule


class Jolka(Model[str]):
    def __init__(
        self,
        path: Path,
    ) -> None:
        super().__init__(
            name=path.name,
        )
        lines = path.read_text().splitlines()
        height, _, width = lines[0].partition("x")
        self.height = int(height)
        self.width = int(width)

        domain = []
        for line in lines[self.height + 1 :]:
            domain.append(line)

        board = lines[1 : self.height + 1]

        self._horizontal_variables: dict[tuple[int, int], tuple[int, Variable[str]]] = {}
        for h in range(self.height):
            start_w = 0
            for w in range(self.width):
                char = board[h][w]
                is_last_char = w + 1 == self.width and char != "#"
                if is_last_char or char == "#":
                    length = w - start_w + int(is_last_char)
                    if length > 1:
                        variable = Variable(
                            domain=[value for value in domain if len(value) == length],
                        )
                        self.add_variable(variable)
                        for i in range(length):
                            self._horizontal_variables[h, start_w + i] = (i, variable)

                    start_w = w + 1

        self._vertical_variables: dict[tuple[int, int], tuple[int, Variable[str]]] = {}
        for w in range(self.width):
            start_h = 0
            for h in range(self.height):
                char = board[h][w]
                is_last_char = h + 1 == self.height and char != "#"
                if is_last_char or char == "#":
                    length = h - start_h + int(is_last_char)
                    if length > 1:
                        variable = Variable(
                            domain=[value for value in domain if len(value) == length],
                        )
                        self.add_variable(variable)
                        for i in range(length):
                            self._vertical_variables[start_h + i, w] = (i, variable)
                    start_h = h + 1

        for h_coords, (h_index, h_variable) in self._horizontal_variables.items():
            for v_coords, (v_index, v_variable) in self._vertical_variables.items():
                if h_coords == v_coords:
                    constraint = IsJolkaRule(
                        h_variable=h_variable,
                        h_index=h_index,
                        v_variable=v_variable,
                        v_index=v_index,
                    )
                    self.add_constraint(constraint)

    def _get_char(
        self,
        coords: tuple[int, int],
    ) -> str:
        char = "#"

        if coords in self._horizontal_variables:
            index, variable = self._horizontal_variables[coords]
            if variable.value is not None:
                return variable.value[index]
            else:
                char = "_"

        if coords in self._vertical_variables:
            index, variable = self._vertical_variables[coords]
            if variable.value is not None:
                return variable.value[index]
            else:
                char = "_"

        return char

    def __str__(self) -> str:
        board = ""

        for h in range(self.height):
            for w in range(self.width):
                value = self._get_char((h, w))
                board += value
            board += "\n"

        return board
