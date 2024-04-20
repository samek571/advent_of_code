class Solution:
    def largestPerimeter(self, nums) -> int:
        
        nums.sort()
        # we generally want to be greedy
        for i in range(len(nums) - 3, -1, -1):

            # triangle definition that has to be satisfied
            # because it can happen that we have 2 large sides and a lot of similarly smaller ones --> we cant take 3 greatest
            if nums[i] + nums[i+1] > nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]

        return 0
