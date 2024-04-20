class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        stt = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} 
        
        n = len(s)
        cnt = 0
        for i in range(n//2):
            if s[i] in stt: cnt+=1
            if s[n-1-i] in stt: cnt-=1
        
        if cnt ==0: return True
        return False
