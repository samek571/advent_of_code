class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #we have 3 states
        '''
        -1 sell --> wait
        0  wait --> wait or buy
        1  buy --> sell or buy
        '''

        @lru_cache
        def dfs(position, i):
            #its the end, as we dive back we sum the rest
            if i >= len(prices): return 0

            #further dfs
            if position == 0:   return max(-prices[i] + dfs(1, i+1), dfs(0, i+1))
            elif position == 1: return max(prices[i] + dfs(-1, i+1), dfs(1, i+1))
            elif position == -1:return dfs(0, i+1)
        
        return dfs(0, 0)    
