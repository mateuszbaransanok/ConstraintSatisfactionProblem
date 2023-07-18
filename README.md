# Constraint Satisfaction Problem

This repository contains an implementation of the Constraint Satisfaction Problem (CSP) framework for educational purposes.
The goal of this project is to explore and evaluate algorithms such as Backtracking and Forward Checking, as well as various heuristics for variable and value selection.


### What is a Constraint Satisfaction Problem (CSP)?

A Constraint Satisfaction Problem involves finding a solution that satisfies a set of constraints or limitations.
It consists of a set of variables, each with a domain of possible values, and a set of constraints that define the relationships between the variables.
The task is to assign values to the variables in such a way that all constraints are satisfied simultaneously.


## Installation

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

* **In order** selects variables in the order they appear in the given CSP instance.
  It follows a sequential approach and assigns values to variables one by one, starting from the first variable in the list.

* **Most constrained** selects the variable with the fewest remaining values in its domain.
  It aims to choose the variable that is most constrained, potentially reducing the search space more quickly.

* **Most constraining** selects the variable involved in the largest number of constraints with other variables.
  It prioritizes the variable that has the most impact on other variables, increasing the chances of finding a solution more efficiently.

* **Random** randomly selects variables from the available options.
  It does not follow any specific order or criteria and can be useful for exploring different search paths.


### Value Selection Heuristics

* **Ascending** selects values in ascending order from the domain of a variable.
  It starts with the smallest value and progresses incrementally.
  It can be useful when the order of values is relevant or when the domain has a natural ordering.

* **Least constraining** prioritizes values that impose the fewest constraints on the remaining unassigned variables.
  It aims to choose values that leave the most options open for subsequent variable assignments, potentially improving the efficiency of the search process.

* **Random** randomly selects values from the available options.
  It does not follow any specific order or criteria and can be useful for exploring different search paths or when the order of values is not significant.


## Games

### Futoshiki

Futoshiki is a logic-based puzzle game that is played on a square grid. 
The objective of the game is to fill in the grid with numbers, satisfying certain rules and constraints. 
Here is a description of the standard Futoshiki puzzle file format:

```text
N
START:
4;0;0;0
0;1;0;4
0;0;2;0
0;3;0;0
REL:
B2;B3
D2;C2
```

The first line of the file contains a single number N, which indicates the size of the puzzle.

Following the line with the text "START:", the representation of the initial state of the puzzle is provided. 
The grid is represented by N lines, each containing N numbers. 
The numbers from 1 to N represent the filled-in values in the puzzle.
If a position contains a value of 0, it signifies that the cell is empty and needs to be filled in during the puzzle-solving process.

The next section of the file contains the lines following the 'REL:' label, which provides information about the relationships between the cells in the puzzle.
It is important to note that each recorded relationship implies that the first (left) cell of the pair should be smaller than the second (right) cell of the pair.
The rows are denoted by consecutive Latin alphabet letters (starting from A), and the columns are represented by consecutive natural numbers (starting from 1).


### Skyscrapper

Skyscraper is a puzzle game that involves arranging buildings on a square grid based on clues provided on the edges of the grid.
The objective is to place buildings in such a way that they meet certain visibility rules. 
Here is a description of the standard Skyscraper puzzle file format:

```text
N
G;1;3;2;3
D;0;2;0;1
L;1;0;0;4
P;2;2;2;2
```

The first line of the file contains a single number N, which indicates the size of the puzzle.

The file includes information about the edges of the puzzle, namely [G] for the top edge, [D] for the bottom edge, [L] for the left edge, and [P] for the right edge. 
Each edge description is followed by a series of numbers from 1 to N. 
If a position contains a value of 0, it means that there is no clue regarding the number of visible buildings from that position. 
When filling in the grid, the buildings are placed from left to right for the top and bottom edges, and from top to bottom for the left and right edges.


### Jolka

Jolka is a word puzzle game that involves filling a grid with words based on given clues. 
The goal is to complete the grid with valid words that intersect with each other correctly.
Here is a description of the standard Jolka puzzle file format:

```text
NxM
____
___#
____
boat
art
need
ban
ore
ate
```

The first line of the file indicates the size of the puzzle grid using the format "NxM", where N represents the number of rows and M represents the number of columns.

The following lines represent the puzzle grid itself, where empty spaces are indicated by underscores (_) and 
blocks (empty positions that cannot be filled with words) are represented by pound signs (#).

After the puzzle grid, the file includes a list of clues.
Each clue corresponds to a word that needs to be filled into the grid, crossing the empty spaces at the corresponding positions. 
The clues are listed one per line.


### Sudoku

Sudoku is a popular logic-based number puzzle that involves filling a 9x9 grid with digits from 1 to 9. 
The goal is to complete the grid so that each row, each column, and each of the nine 3x3 sub-grids (also known as "boxes")
contains all the digits from 1 to 9 without any repetition. 

Here is a description of the standard Sudoku puzzle file format:

```text
625..1..8.7..8...68........2....4....4..1.3........1.......7.32.....6.9..84.3....
625371948473985216819462753231794685547618329968523174196857432352146897784239561
```

The first line of the file represents the initial state of the puzzle, where each dot (.) represents an empty cell that needs to be filled. 
The numbers represent the pre-filled digits in the grid.

The second line of the file represents the optional solution to the puzzle, where each digit corresponds to a filled-in cell in the grid, 
following the Sudoku rules of no repetition in rows, columns, and boxes. 
It is important to note that the solution line is not always present in every Sudoku puzzle file. 
Some files may only contain the initial state of the puzzle without the corresponding solution.


## Run Experiments

The purpose of the experiments is to evaluate all combinations of models, methods, and heuristics for your project.
The results will be saved in the [experiments](experiments) folder for further analysis.

To run the script, use the following command in your terminal or command prompt:

```bash
PYTHONPATH=. python scripts/run_experiments.py
```

Feel free to customize the script or experiment configurations as needed for your specific project requirements.


## Contribution
Contributions are very welcome.
Tests can be run with [tox](https://tox.wiki/en/latest/), please ensure the coverage at least stays the same before you submit a merge request.


## License
Distributed under the terms of the [MIT](https://opensource.org/license/mit/) license, this is free and open source software.


## Issues
If you encounter any problems, please leave [issue](../../issues/new), along with a detailed description.
