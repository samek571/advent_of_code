class Solution:
    def maxProfit(prices) -> int:
        maxi, mini = 0, float('inf')

        for i in prices:
            mini = min(mini, i)
            maxi = max(maxi, i-mini)

        return maxi

    print(maxProfit([7,1,5,3,6,4]))
    print(maxProfit([7,6,4,3,1]))
