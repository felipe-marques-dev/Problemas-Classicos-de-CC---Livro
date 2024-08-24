def fib(n: int) -> int: 
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range(1,n):
        # 1, 1 ( last = 1, next = 1)
        # 1, 2 ( last = 1, next = 1 + 1)
        # 2, 3  (last = 2, next = 1 + 2)
        # 3, 5  (last = 3, next = 2 + 3)
        last, next = next, last + next
    return next

print(fib(4300))