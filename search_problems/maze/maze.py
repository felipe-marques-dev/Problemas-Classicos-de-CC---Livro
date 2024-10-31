from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
# from  generic_search import dfs, bfs, node_to_path, astar, Node


class Cell(str, Enum):
    EMPTY = ""
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"


class MazeLocation(NamedTuple):
    row: int
    column: int


class Maze:
    def __init__(self, rows: int = 10, columns: int = 10, sparseness: float = 0.2, start:MazeLocation = MazeLocation(0,0), 
                 goal: MazeLocation = MazeLocation(9,9)) -> None:
        # inicializa as variaveis de instância basicas
        self._rows: int = rows
        self._columns: int = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        # preenche a grade com células vazias
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        #preenche a grade com celulas bloqueadas bloqueadas
        self._randomly_fill(rows, columns, sparseness)
        # preenche as posicoes inicial e final
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    
    def _randomly_fill(self, rows: int, columns: int, sparseness: float):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

        
    # devolve uma versao do labirinto com uma formataca elegante para exibicao
    def __str__(self) -> str:
        output: str = ""
        for row in self._grid:
            output += " ".join([c.value for c in row]) + "\n"
        return output
    

maze: Maze = Maze()
print(maze)