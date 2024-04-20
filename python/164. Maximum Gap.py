class Solution:
    def maximumGap(nums) -> int:

        if len(nums) < 2:
            return 0

        else:
            nums = sorted(nums, reverse=True)
            maximal = 0

            for i in range(1, len(nums)):
                if nums[i-1] - nums[i] > maximal and i <= len(nums):
                    maximal = nums[i-1] - nums[i]
            return maximal
    print(maximumGap([9,4,0,7]))
    print(maximumGap([12, 40, 18, 90, 44, 22]))
    print(maximumGap([30266,74974,6275,5926]))