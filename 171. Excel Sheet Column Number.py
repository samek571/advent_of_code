class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        cnt = 0

        l = len(columnTitle)-1
        ei = 0
        while l>-1:
            cnt += (ord(columnTitle[ei])-64) * 26**l
            l-=1
            ei+=1
        
        return cnt
