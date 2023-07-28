from functools import lru_cache
class Solution:
    def combinationSum3(self, k: int, n: int):# -> List[List[int]]:
        if n > 45:
            return []

        tmp = 0
        for i in range(9, 9 - k + 1 - 1, -1):
            tmp += i
        if tmp < n:
            return []

        res = []
        @lru_cache(maxsize=None)
        def dfs(total, path, start):
            if total == n and len(path) == k:
                res.append(list(path))
                return
            elif total > n or len(path) >= k:
                return

            for i in range(start, 10):
                dfs(total + i, tuple(path) + (i,), i + 1)

        dfs(0, (), 1)

        return res

def main():
    sol = Solution()
    print(sol.combinationSum3(3, 30))
    print(sol.combinationSum3(3, 24))
    print(sol.combinationSum3(3, 25))
    print(sol.combinationSum3(4, 30))
    print(sol.combinationSum3(4, 31))
    print(sol.combinationSum3(4, 31))
    print(sol.combinationSum3(9, 44))
    print(sol.combinationSum3(9, 45))

if __name__ == "__main__": main()