from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

V = TypeVar('V') # tipo para variavel
D = TypeVar('D') # variavel para dominio


# Classe-base para todas as restrições
class Constraint(Generic[V, D], ABC):
    # as variavei sujetias a restrição
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    # deve ser sobrescrito pelas subclassses
    @abstractmethod
    def satisfied(self, assignment: Dict[V,D]) -> bool:
        pass


# Um problema de satisfação de restrições é composto de variáveis do tipo V
# que tem intervalos de valores conhecidos como dominios do tipo D e restrições
# que determinam se a escolha de dominio de uma variavel em particular é valida
class CSP(Generic[V, D]):
    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        self.variables: List[V] = variables # variaveis a serem restringidas
        self.domains: Dict[V, List[D]] = domains #dominio de cada variavel
        self.constraints: Dict[V, List[Constraint[V,D]]] = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it.")
        
    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)
     

