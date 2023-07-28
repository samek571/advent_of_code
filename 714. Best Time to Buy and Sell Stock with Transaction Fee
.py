class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        @lru_cache
        def dfs(buying, i):
            #its the end, as we dive back we sum the rest
            if i >= len(prices): return 0


            ans = dfs(buying, i+1)
            #further dfs
            if buying: ans = max(ans, -prices[i] + dfs(False, i+1))
            else: ans = max(ans, prices[i]-fee + dfs(True, i+1))

            return ans

        return dfs(True, 0)    
