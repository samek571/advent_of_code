from functools import lru_cache
@lru_cache(None)
def fib(n: int) -> int:
    if n==0:
        return 0
    elif n<3:
        return 1

    else:
        return fib(n-1)+fib(n-2)

print(fib(466))
print(fib(0))
print(fib(2))
print(fib(3))
print(fib(4))