from enum import Enum
from typing import List, NamedTuple
import random


class Cell(str, Enum):
    EMPTY = "0"
    BLOCKED = '\033[31m'+'X'+'\033[0;0m'
    PATH = '\033[32m'+'*'+'\033[0;0m' 


class MazeLocation(NamedTuple):
    row: int
    column: int


mapValues: int = 9
goalLocation: int = mapValues - 1
class Board:
    def __init__(self, rows: int = mapValues, columns: int = mapValues, difficulty: float = 0.1) -> None:
        # inicializa as variaveis de instância basicas
        self._rows: int = rows
        self._columns: int = columns
        self._difficulty: int = difficulty
        # preenche a grade com células vazias
        self._grid = [[0 for c in range(columns)] for r in range(rows)]

    def generateRandomNumbers(self):
        randomNumber = random.randrange(1,9)
        print(randomNumber)
        return randomNumber

    def is_valid(self, randomNumber, row, column):
        if randomNumber in self._grid[row]:                   
            return False

        for i in range(9):
            if self._grid[i][column] == randomNumber:
                return False
        
        return True

    def randomly_fill(self):
            for row in range(self._rows):
                for column in range(self._columns):
                    randomNumber = board.generateRandomNumbers()
                    if self._grid[row][column] !=  randomNumber and random.uniform(0, 1.0) > self._difficulty and board.is_valid(randomNumber, row, column) and board.sucessors(row, column, randomNumber):
                        self._grid[row][column] = randomNumber
                    else: 
                        self._grid[row][column] = 0
            return True 

    # Identifica os espaços disponiveis ao redor da localização atual
                     # Identifica os espaços disponíveis ao redor da localização atual
    def sucessors(self, row, column, number):
    
        # Verifica a célula abaixo (row + 1)
        if row + 1 < len(self._grid) and self._grid[row + 1][column] == number:
            return False
    
        # Verifica a célula acima (row - 1)
        if row - 1 >= 0 and self._grid[row - 1][column] == number:
            return False    
    
        # Verifica a célula à direita (column + 1)
        if column + 1 < len(self._grid[row]) and self._grid[row][column + 1] == number:
            return False
    
        # Verifica a célula à esquerda (column - 1)
        if column - 1 >= 0 and self._grid[row][column - 1] == number:
            return False
    
        # Verifica a célula diagonal superior esquerda (row - 1, column - 1)
        if row - 1 >= 0 and column - 1 >= 0 and self._grid[row - 1][column - 1] == number:
            return False
    
        # Verifica a célula diagonal superior direita (row - 1, column + 1)
        if row - 1 >= 0 and column + 1 < len(self._grid[row]) and self._grid[row - 1][column + 1] == number:
            return False
    
        # Verifica a célula diagonal inferior esquerda (row + 1, column - 1)
        if row + 1 < len(self._grid) and column - 1 >= 0 and self._grid[row + 1][column - 1] == number:
            return False
    
        # Verifica a célula diagonal inferior direita (row + 1, column + 1)
        if row + 1 < len(self._grid) and column + 1 < len(self._grid[row]) and self._grid[row + 1][column + 1] == number:
            return False

        # Se nenhuma das comparações retornar False, significa que o número pode ser colocado
        return True
# devolve uma versão do tabuleiro com uma formatação elegante para exibição
    def __str__(self) -> str:
        output: str = ""
        for row in self._grid:
            output += " ".join([str(c) for c in row]) + "\n"
        return output 


class SudokuSolver():
    def __init__(self):
        pass

    def solver(self):
        pass


if __name__ == "__main__":
    board = Board()
    randomNumber = board.generateRandomNumbers()
    print(board.randomly_fill())
    print(board)
