class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        dp = list(arr)
        for i, a in enumerate(arr):
            if i > 1: dp[i] += (i // 2) * (arr[i] + arr[i-1]) + dp[i - 2]
        return sum(dp)
