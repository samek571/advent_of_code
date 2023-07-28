class Solution:
    def maxSubarraySumCircular(nums) -> int:

        totalsum=0
        allnegative = True
        for i in nums:
            totalsum+=i
            if i>0: allnegative = False


        if allnegative: return max(nums)


        dpmax, dpmin = [0]*(len(nums)), [0]*(len(nums))
        dpmax[0], dpmin[0] = nums[0], nums[0]
        step = 0
        while step < len(nums):

            dpmax[step] = max(dpmax[step-1]+nums[step],nums[step])
            dpmin[step] = min(dpmin[step-1]+nums[step],nums[step])
            step+=1

        return max(totalsum-min(dpmin), max(dpmax))

    print(maxSubarraySumCircular([1,-2,3,-2]))
    print(maxSubarraySumCircular([5,-3,5]))
    print(maxSubarraySumCircular([-3,-2,-3]))