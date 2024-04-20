class Solution:
    def wordBreak(s, wordDict) -> bool:
        n = len(s)
        dp = [False for _ in range(n + 1)]
        dp[0] = True

        for i in range(n):
            if dp[i]:
                for w in wordDict:
                    if s[i:i + len(w)] == w:
                        dp[i + len(w)] = True
        return dp[-1]