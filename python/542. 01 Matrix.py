import copy
import math

class Solution:
    def updatenewmatrix(mat):

        hl = len(mat)
        vl = len(mat[0])

        if hl == 0: return mat
        newmat = [[math.inf if mat[i][j] != 0 else 0 for j in range(vl)] for i in range(hl)]

        for row in range(hl):
            for col in range(vl):
                if mat[row][col] == 0: newmat[row][col] = 0
                else:
                    if row > 0: newmat[row][col] = min(newmat[row-1][col]+1, newmat[row][col])
                    if col > 0: newmat[row][col] = min(newmat[row][col-1]+1, newmat[row][col])


        for row in range(hl-1, -1, -1):
            for col in range(vl-1, -1, -1):

                if row < hl-1: newmat[row][col] = min(newmat[row+1][col]+1, newmat[row][col])
                if col < vl-1: newmat[row][col] = min(newmat[row][col+1]+1, newmat[row][col])


        for i in newmat:
            print(i)
        return newmat

    print(updatenewmatrix([[0,0,0],[0,1,0],[1,1,1]]))
    print(updatenewmatrix([[0,0,0],[0,1,1],[1,1,1]]))
    #print(updatenewmatrix([0]))
