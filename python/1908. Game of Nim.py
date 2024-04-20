class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        

        #algo that checks if there is good amount of odd numbers
        s = 0
        for p in piles:
            s ^= p
        
        return s
        
