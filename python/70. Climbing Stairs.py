from functools import lru_cache
@lru_cache(None)
def climbStairs(n: int) -> int:
    if n<4:
        return n

    else:
        return climbStairs(n-1) + climbStairs(n-2)


print(climbStairs(7))