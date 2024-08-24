from typing import Dict
memo: Dict[int, int] = {0:0, 1:1} # nossos casos de base

def fib(n: int) -> int:
    if n not in memo:
        # memoizacao
        memo[n] = fib(n-1) - fib(n-2)
    return memo[n]

print(fib(400))
