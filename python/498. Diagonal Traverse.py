class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        #edge cases till mn<3
        # define ur and ld fxs, its change ifthere is one zero at x or yle
        res=[] ; n=len(mat[0]) ; m=len(mat) ; i=j=0; direction=1

        # def up_right(i,j):
        #     if i == 0 or j==m:
        #         if i*j == m*n: return
        #         else: down_left(i,j+1)
            
        #     else: 
        #         res.append(mat[i][j])
        #         up_right(i+1,j+1)
        

        # def down_left(i,j):
        #     if j==0 or i==n:
        #         up_right(i+1,j)
            
        #     else:
        #         res.append(mat[i][j])
        #         down_left(i-1,j-1)


        
        # up_right(0,0)
        # return res

        while len(res) < m * n:
                res.append(mat[i][j])
                if direction == 1:
                    if i == 0 or j == n - 1:
                        if j == n - 1:
                            i += 1
                        else:
                            j += 1
                        direction = -1
                    else:
                        i -= 1
                        j += 1
                else:
                    if i == m - 1 or j == 0:
                        if i == m - 1:
                            j += 1
                        else:
                            i += 1
                        direction = 1
                    else:
                        i += 1
                        j -= 1

        return res
