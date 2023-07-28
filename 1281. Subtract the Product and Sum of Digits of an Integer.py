class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a, b = 0, 1
        
        for i in str(n):
            i= int(i)

            a+=i
            b*=i
        
        return b-a
