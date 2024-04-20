class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        o=0
        #if n==1: return mat[0][0]

        for i in range(n//2):
            a,b = mat[i][i], mat[i][n-1-i]
            c,d = mat[n-1-i][n-1-i] , mat[n-1-i][i]
   
            o+=a+b+c+d
        
        if n%2==1: 
            return o+mat[n//2][n//2]
        else: return o
