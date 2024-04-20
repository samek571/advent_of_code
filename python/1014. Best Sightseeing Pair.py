class Solution:
    def maxScoreSightseeingPair(values) -> int:

        #O(n^2) & O(1)
        # maximaler=values[0]+values[1]-1
        # for i in range(len(values)-1):
        #     for j in range(i+1, len(values)):
        #         maximaler = max(maximaler, values[i] + values[j] + i -j)
        #
        # return maximaler

        #O(n) & O(1)
        dp = [0]*len(values)
        dp[0] = values[0]
        aks=0

        for i in range(1, len(values)):
            dp[i] = max(dp[i-1], values[i-1]-1+i)
            aks = max(aks, dp[i] + values[i]-i)

        return aks
    print(maxScoreSightseeingPair([8,1,5,2,6]))
    print(maxScoreSightseeingPair([8,1,5,2,6,56]))
    print(maxScoreSightseeingPair([1,2]))