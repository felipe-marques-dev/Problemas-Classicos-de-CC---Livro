from functools import lru_cache



@lru_cache(maxsize=None) # salva resultados anteriores em cache, None quer dizer que nao ha um limite
def fib(n: int) -> int:

    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

print(fib(1000))
