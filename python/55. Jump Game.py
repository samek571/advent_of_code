class Solution:
    def canJump(nums) -> bool:
        req = 0
        for i in range(len(nums)-1,-1,-1):

            if nums[i] < req:req += 1
            else: req = 1

        return req == 1

    print(canJump([2,3,1,1,4]))
    print(canJump([3,2,1,0,4]))