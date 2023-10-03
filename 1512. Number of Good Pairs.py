class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        x = collections.Counter(nums)

        res = 0
        for key, val in x.items():
            res+=val * (val-1)//2

        return res
