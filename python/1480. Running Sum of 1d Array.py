class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        var = 0
        for i in range(len(nums)):
            nums[i] = nums[i]+var
            var = nums[i]
        
        return nums
