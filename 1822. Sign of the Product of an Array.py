class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        o=1
        for i in nums:
            if i == 0: return 0
            elif i<0: o*=-1
        
        return o
