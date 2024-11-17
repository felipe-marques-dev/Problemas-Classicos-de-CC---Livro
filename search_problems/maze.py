from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
# from  generic_search import dfs, bfs, node_to_path, astar, Node
from generic_search import *


class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = '\033[31m'+'X'+'\033[0;0m'
    START = "S"
    GOAL = "G"
    PATH = '\033[32m'+'*'+'\033[0;0m' 


class MazeLocation(NamedTuple):
    row: int
    column: int


mapValues: int = 20
goalLocation: int = mapValues - 1
class Maze:
    def __init__(self, rows: int = mapValues, columns: int = mapValues, sparseness: float = 0.2, start:MazeLocation = MazeLocation(0,0), 
                 goal: MazeLocation = MazeLocation(goalLocation,goalLocation)) -> None:
        # inicializa as variaveis de instância basicas
        self._rows: int = rows
        self._columns: int = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        # preenche a grade com células vazias
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        # preenche a grade com celulas bloqueadas
        self._randomly_fill(rows, columns, sparseness)
        # preenche as posicoes inicial e final
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    # Preenche campos do labirinto com espaços bloquados aleatoriamente    
    def _randomly_fill(self, rows: int, columns: int, sparseness: float):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED


    def goal_test(self, ml: MazeLocation) -> bool:
        return ml == self.goal

    # Identifica os espaços disponiveis ao redor da localização atual
    def sucessors(self, ml: MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []
        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row+1, ml.column))
        if ml.row - 1 >= 0 and self._grid[ml.row-1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row-1, ml.column))
        if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column + 1))
        if ml.column - 1 >= 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column -1))
        return locations

    def mark(self, path: List[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path: List[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def euclidian_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:
        def distance(ml: MazeLocation) -> float:
            xdist: int = ml.column - goal.column
            ydist: int = ml.row - goal.row
            return sqrt((xdist * xdist) + (ydist * ydist))
        return distance
    # devolve uma versão do labirinto com uma formatação elegante para exibição
    def __str__(self) -> str:
        output: str = ""
        for row in self._grid:
            output += " ".join([c.value for c in row]) + "\n"
        return output 
    
def manhattan_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:
        def distance(ml: MazeLocation) -> float:
            xdist: int = abs(ml.column - goal.column)
            ydist: int = abs(ml.row - goal.row)
            return(xdist + ydist)
        return distance


if __name__ == "__main__":
    # teste da A*
    m: Maze = Maze()
    print(m)
    print("="*40)
    distance: Callable[[MazeLocation], float] = manhattan_distance(m.goal)
    solution1: Optional[Node[MazeLocation]] = astar(m.start, m.goal_test, m.sucessors, distance)

    if solution1 is None:
        print("No solution found using A*")
    else:
        path1: List[MazeLocation] = node_to_path(solution1)
        m.mark(path1)
        print(m)
        m.clear(path1)