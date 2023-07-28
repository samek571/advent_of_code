import collections
from functools import lru_cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        cache = collections.defaultdict(int)

        @lru_cache(maxsize=None)
        def dfs(substring):
            if substring not in cache:
                for char in set(substring):
                    start, end = substring.find(char), substring.rfind(char)
                    #basically nice way of saying that if it meets, that means its palindrome 
                    # (each palindrome is known that the first and last character is equal and therefore not necesarry)
                    cache[substring] = max(cache[substring], 1 if start == end else 2 + dfs(substring[start + 1:end]))
            
            return cache[substring]



        return dfs(s)
