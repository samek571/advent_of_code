class Solution:
    #cached dfs would be faster
    def coinChange(self, coins: List[int], amount: int) -> int:

        
        queue = collections.deque([(amount, 0)]) 
        visited = set()
        while queue:
            remaining_amount, num_coins = queue.popleft()
            
            # bfs makes us find the lowest amount 
            if remaining_amount == 0:
                return num_coins
            
            for coin in coins:
                new_remaining_amount = remaining_amount - coin
                
                # Skip if new case is useless
                if new_remaining_amount in visited or new_remaining_amount < 0:
                    continue
                
                queue.append((new_remaining_amount, num_coins + 1))
                visited.add(new_remaining_amount)
                    
        return -1
