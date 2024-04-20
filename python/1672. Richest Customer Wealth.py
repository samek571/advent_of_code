class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        outpur = 0
        for i in accounts:
            outpur = max(outpur, sum(i))

        return outpur
