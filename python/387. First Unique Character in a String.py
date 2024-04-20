class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hsh = collections.defaultdict(int)

        for i, char in enumerate(s):
            if char not in hsh: hsh[char] = i
            #every duplicate gets basically removed
            else: hsh[char] = -1
        
        o = float('inf')
        for val in hsh.values():
            
            if val != -1: #speaking strictly non duplicates
                o = min(o, val)
        
        return -1 if o == float('inf') else o
        
