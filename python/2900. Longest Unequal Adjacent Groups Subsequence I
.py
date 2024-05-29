class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1]*n
        prev = [-1]*n
        for i in range(1,n):
            for j in range(i):
                if groups[i] != groups[j] and dp[i] < dp[j]+1:
                    dp[i] = 1+dp[j]
                    prev[i] = j

        l = max(dp)
        l_index = dp.index(l)

        res=[]
        while l_index != -1:
            res.append(words[l_index])
            l_index = prev[l_index]

        return res[::-1]
