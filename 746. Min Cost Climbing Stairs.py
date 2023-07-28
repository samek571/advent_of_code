class Solution:
    def minCostClimbingStairs(cost) -> int:

        for i in range(2, len(cost)): cost[i] += min(cost[i-1], cost[i-2])

        return min(cost[len(cost)-1], cost[len(cost)-2])

    print(minCostClimbingStairs([10,15,20]))