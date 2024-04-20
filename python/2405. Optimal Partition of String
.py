class Solution:

    '''sliding window clear as ever'''

    def partitionString(self, s: str) -> int:
        def isUnique(s): return len(set(s)) == len(s)
                    
        left = 0 ; res = 0
        
        for right in range(1,len(s)+1):
            if not isUnique(s[left:right]):
                res += 1
                left = right-1
                
        return res+1
