class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        #wrong
        # hsh={}

        # for i in range(len(s)):
        #     if s[i] not in hsh:
        #         hsh[s[i]] = t[i]
            
        #     else:
        #         if hsh[s[i]] != t[i]: return False
        
        # return True

        #zip makes bothsided bijection 
        return len(set(s))==len(set(zip(s,t)))==len(set(t))
