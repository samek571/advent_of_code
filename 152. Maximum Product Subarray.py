class Solution:
    def maxProduct(nums):
        maxi = mini = ans = nums[0]
        for i in nums[1:]:
            maxi, mini = max(i, i*maxi, i*mini), min(i, i*maxi, i*mini)
            ans = max(ans, maxi)

        return ans


    print(maxProduct([2,3,3,1,-2,6,6,6,6]))
    print(maxProduct([2,3,3,1,-2,6,6,6,-6]))
    print(maxProduct([2,3,3,1,-2,-6,6,6,-6]))
    print(maxProduct([2,3,3,1,-2,-6,-6,6,6]))