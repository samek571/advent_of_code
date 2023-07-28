class Solution:
    def jump(nums) -> int:
        n = len(nums)
        if n == 1: return 0
        dp, furthest_index = [0] * n, 0

        for i in range(1, n):
            while i > furthest_index + nums[furthest_index] and furthest_index < i: furthest_index += 1

            dp[i] = dp[furthest_index] + 1

        return dp[-1]

    print(jump([2,3,1,1,4,8,1,1,2,0,4,2,2,0,9]))
    print(jump([2,3,1,1,4]))