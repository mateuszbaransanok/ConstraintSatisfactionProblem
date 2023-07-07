# Constraint Satisfaction Problem

This repository contains an implementation of the Constraint Satisfaction Problem (CSP) framework for educational purposes.
The goal of this project is to explore and evaluate algorithms such as Backtracking and Forward Checking, as well as various heuristics for variable and value selection.


## What is a Constraint Satisfaction Problem (CSP)?

A Constraint Satisfaction Problem involves finding a solution that satisfies a set of constraints or limitations.
It consists of a set of variables, each with a domain of possible values, and a set of constraints that define the relationships between the variables.
The task is to assign values to the variables in such a way that all constraints are satisfied simultaneously.


# Installation

To install the project, follow these steps:

1. Clone the repository.
2. Create a Python 3.10+ environment.


## Algorithms

* **Backtracking** is a systematic approach that explores the search space by trying out different assignments for
  variables and backtracking whenever a constraint violation occurs.
  It uses depth-first search and can be enhanced with heuristics to improve efficiency.

* **Forward Checking** is an enhancement to the basic backtracking algorithm.
  It performs constraint propagation by checking the consistency of assigned values and updating the domains of unassigned variables.
  This helps in reducing the search space by eliminating inconsistent choices early.


## Selection Heuristics

### Variable Selection Heuristics

* **In order**: This heuristic selects variables in the order they appear in the given CSP instance.
  It follows a sequential approach and assigns values to variables one by one, starting from the first variable in the list.

* **Most constrained**: This heuristic selects the variable with the fewest remaining values in its domain.
  It aims to choose the variable that is most constrained, potentially reducing the search space more quickly.

* **Most constraining**: This heuristic selects the variable involved in the largest number of constraints with other variables.
  It prioritizes the variable that has the most impact on other variables, increasing the chances of finding a solution more efficiently.

* **Random**: This heuristic randomly selects variables from the available options.
  It does not follow any specific order or criteria and can be useful for exploring different search paths.


### Value Selection Heuristics

* **Ascending**: This heuristic selects values in ascending order from the domain of a variable.
  It starts with the smallest value and progresses incrementally.
  It can be useful when the order of values is relevant or when the domain has a natural ordering.

* **Least constraining**: This heuristic prioritizes values that impose the fewest constraints on the remaining unassigned variables.
  It aims to choose values that leave the most options open for subsequent variable assignments, potentially improving the efficiency of the search process.

* **Random**: This heuristic randomly selects values from the available options.
  It does not follow any specific order or criteria and can be useful for exploring different search paths or when the order of values is not significant.


### Run Experiments

The purpose of the experiments is to evaluate all combinations of models, methods, and heuristics for your project.
The results will be saved in the [experiments](experiments) folder for further analysis.

To run the script, use the following command in your terminal or command prompt:

```bash
PYTHONPATH=. python scripts/run_experiments.py
```

Feel free to customize the script or experiment configurations as needed for your specific project requirements.


# Contribution
Contributions are very welcome.
Tests can be run with [tox](https://tox.wiki/en/latest/), please ensure the coverage at least stays the same before you submit a merge request.


# License
Distributed under the terms of the [MIT](https://opensource.org/license/mit/) license, this is free and open source software.


# Issues
If you encounter any problems, please email me at <mateusz.baran.sanok@gmail.com>, along with a detailed description.
