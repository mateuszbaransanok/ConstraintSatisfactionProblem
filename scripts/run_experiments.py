import json
from datetime import datetime
from itertools import product

from csp import PROJECT_DIR
from csp.heuristics.value.ascending import AscendingValues
from csp.heuristics.value.least_constraining import LeastConstrainingValues
from csp.heuristics.variable.in_order import InOrderVariables
from csp.heuristics.variable.most_constrained import MostConstrainedVariables
from csp.heuristics.variable.most_constraining import MostConstrainingVariables
from csp.methods.backtracking import Backtracking
from csp.methods.forward_checking import ForwardChecking
from csp.models.futoshiki import Futoshiki
from csp.models.jolka import Jolka
from csp.models.skyscrapper import Skyscrapper
from csp.models.sudoku import Sudoku

FIND_ALL_SOLUTIONS = False

futoshiki = [
    "futoshiki_4_0.txt",
    "futoshiki_4_1.txt",
    "futoshiki_4_2.txt",
    "futoshiki_4_3.txt",
    "futoshiki_4_4.txt",
    "futoshiki_4_5.txt",
    "futoshiki_4_6.txt",
    "futoshiki_4_7.txt",
    "futoshiki_5_0.txt",
    "futoshiki_5_1.txt",
    "futoshiki_5_2.txt",
    "futoshiki_5_3.txt",
    "futoshiki_5_5.txt",
    "futoshiki_5_6.txt",
    "futoshiki_5_7.txt",
]

skyscrapper = [
    "skyscrapper_4_0.txt",
    "skyscrapper_4_1.txt",
    "skyscrapper_4_2.txt",
    "skyscrapper_4_3.txt",
    "skyscrapper_4_4.txt",
    "skyscrapper_4_5.txt",
    "skyscrapper_4_6.txt",
    "skyscrapper_4_7.txt",
    "skyscrapper_4_8.txt",
    "skyscrapper_4_9.txt",
    "skyscrapper_5_0.txt",
    "skyscrapper_5_1.txt",
    "skyscrapper_5_3.txt",
    "skyscrapper_5_4.txt",
    "skyscrapper_5_5.txt",
    "skyscrapper_5_6.txt",
    "skyscrapper_5_7.txt",
    "skyscrapper_5_8.txt",
    "skyscrapper_5_9.txt",
]

jolka = [
    "jolka_0.txt",
    "jolka_1.txt",
]

sudoku = [
    "sudoku_0_0.txt",
    "sudoku_0_1.txt",
    "sudoku_0_2.txt",
    "sudoku_0_3.txt",
    "sudoku_0_4.txt",
    "sudoku_1_0.txt",
    "sudoku_1_1.txt",
    "sudoku_1_2.txt",
    "sudoku_1_3.txt",
    "sudoku_1_4.txt",
]

models = [
    *(Futoshiki(PROJECT_DIR / "data/futoshiki" / name) for name in futoshiki),
    *(Skyscrapper(PROJECT_DIR / "data/skyscrapper" / name) for name in skyscrapper),
    *(Jolka(PROJECT_DIR / "data/jolka" / name) for name in jolka),
    *(Sudoku(PROJECT_DIR / "data/sudoku" / name) for name in sudoku),
]

methods = [
    Backtracking,
    ForwardChecking,
]

variable_heuristics = [  # type: ignore[var-annotated]
    InOrderVariables(),
    MostConstrainedVariables(),
    MostConstrainingVariables(),
]

value_heuristics = [  # type: ignore[var-annotated]
    AscendingValues(),
    LeastConstrainingValues(),
]

if __name__ == "__main__":
    date = datetime.now().strftime("%Y%m%d_%H%M%S")
    parameters = list(product(methods, models, variable_heuristics, value_heuristics))
    for i, (method, model, variable_heuristic, value_heuristic) in enumerate(parameters, start=1):
        algorithm = method(
            model=model.copy(),
            variable_heuristic=variable_heuristic,
            value_heuristic=value_heuristic,
            find_all_solutions=FIND_ALL_SOLUTIONS,
        )
        print("=" * 50)
        print("Experiment:", i, "/", len(parameters))
        print("Model:", algorithm.model.__class__.__name__, "-", algorithm.model.name)
        print("Method:", algorithm.__class__.__name__)
        print("Variable heuristic:", algorithm.variable_heuristic.__class__.__name__)
        print("Value heuristic:", algorithm.value_heuristic.__class__.__name__)

        algorithm.start()

        print("=" * 50)
        for solution_num, solution in enumerate(algorithm.solutions, start=1):
            print(solution.model)
            print("Solution:", solution_num, "/", len(algorithm.solutions))
            print("Iterations:", solution.iterations)
            print("Backtracks:", solution.backtracks)
            print("Time:", solution.time)
            print("-" * 50)

            result = {
                "model": algorithm.model.__class__.__name__,
                "name": algorithm.model.name,
                "method": algorithm.__class__.__name__,
                "variable_heuristic": algorithm.variable_heuristic.__class__.__name__,
                "value_heuristic": algorithm.value_heuristic.__class__.__name__,
                "iterations": solution.iterations,
                "backtracks": solution.backtracks,
                "time": solution.time,
            }
            save_path = PROJECT_DIR.joinpath(f"experiments/results_{date}.jsonl")
            save_path.parent.mkdir(parents=True, exist_ok=True)
            with save_path.open(mode="a") as file:
                file.write(json.dumps(result) + "\n")

        if not algorithm.solutions:
            print("There is no solution")
            print("-" * 50)

        if FIND_ALL_SOLUTIONS:
            print("Total iterations:", algorithm.iterations)
            print("Total backtracks:", algorithm.backtracks)
            print("Total time:", algorithm.end_time - algorithm.start_time)
            print("=" * 50)
