class Solution:
    def longestCommonSubsequence(text1: str, text2: str) -> int:
        N = len(text1)
        M = len(text2)
        memo = {}

        def helper(i,j):
            if i == N or j == M:return 0

            key = (i,j)

            if key in memo: return memo[key]
            if text1[i] == text2[j]: memo[key] = 1 + helper(i+1, j+1)
            else: memo[key] = max(helper(i+1,j), helper(i, j+1))

            return memo[key]

        return helper(0,0)