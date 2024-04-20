class Solution:
    def numWays(self, n: int, k: int) -> int:
        
        cache = {}
        @lru_cache
        def dfs(n):
            if n in cache:
                return cache[n]
            if n == 1:
                return k
            if n == 2:
                return k*k

            res = (k-1)*(dfs(n-1)+dfs(n-2))
            cache[n] = res
            return res

        return dfs(n)
