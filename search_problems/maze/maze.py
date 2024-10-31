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


