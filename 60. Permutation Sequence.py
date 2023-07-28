import  math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
       

        k, alles, output = k-1, [i for i in range(1,n+1)], ''
        # while n>0:
        #     n-=1
        #     i , k = divmod(k, math.factorial(n))
        #     removed = alles.pop(i)
        #     output += str(removed)
        
        def dfs(n,k):
            nonlocal alles
            nonlocal output
            
            if n==1: 
                output += str(alles[0])
                return 
            
            n-=1
            i , k = divmod(k, math.factorial(n))
            removed = alles.pop(i)
            output += str(removed)

            dfs(n, k)
            return

        dfs(n,k)
        return output
