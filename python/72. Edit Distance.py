class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # levinshtien distance

        # vars
        m = len(word1) + 1
        n = len(word2) + 1

        dp = [[0 for _ in range(n)] for _ in range(m)]

        # base cases
        # here for an empty string
        # you just need to insert or delete
        # in order to get resultant, so i operations(ops)
        # watch video reference if more clarity needed
        for i in range(m):
            dp[i][0] = i

        for j in range(n):
            dp[0][j] = j

        # Main Loop
        for i in range(1, m):
            for j in range(1, n):

                # same last char then just
                # remove both chars(no need to '+1')
                # again watch video reference for more clarity
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # else get the minimum of delete op
                    # insert op, or sub op
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

        # usual dp return
        return dp[-1][-1]