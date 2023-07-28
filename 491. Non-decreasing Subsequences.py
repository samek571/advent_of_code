class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        bbc=set()

        def dfs(idx, curr, prev):
            if idx == len(nums):
                if len(curr) > 1:
                    bbc.add(tuple(curr))
                return

            if prev <= nums[idx]:
                dfs(idx+1, curr+[nums[idx]], nums[idx])

            dfs(idx+1, curr, prev)

        dfs(0, [], -1*float("inf"))
        return list(bbc)
