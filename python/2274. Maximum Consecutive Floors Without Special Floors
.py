class Solution:
    def maxConsecutive(self, bottom: int, top: int, nums: List[int]) -> int:

        nums = [bottom-1] +sorted(nums)+ [top+1]

        maximal = 0
        for i in range(1, len(nums)):
            maximal = max(nums[i] - nums[i-1]-1, maximal)


        return maximal
