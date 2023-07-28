from collections import defaultdict
from functools import lru_cache
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        @lru_cache(maxsize=None)
        # (length, count)
        def dfs(i):
            if i < 0:
                return (0, 0)

            subsequences = defaultdict(int)
            subsequences[0] = 1

            #the magic of postorder dfs (backtracking)
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i]:
                    length, count = dfs(j)
                    subsequences[length] += count

            longest = max(subsequences)
            return (longest + 1, subsequences[longest])


        subsequences = [dfs(i) for i in range(len(nums) - 1, -1, -1)]
        return max(subsequences)[0]