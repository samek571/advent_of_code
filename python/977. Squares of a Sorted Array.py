class Solution:
    def sortedSquares(nums):

        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]

        return sorted(nums)
    print(sortedSquares([-4,-1,0,3,10]))
    print(sortedSquares([-7,-3,2,3,11]))