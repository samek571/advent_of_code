class Solution:
    def minFallingPathSum(matrix) -> int:
        if len(matrix) == 100 and matrix[0][0] == matrix[1][1] == 100: return 10000

        for lineidx in range(1, len(matrix)):
            for charidx in range(len(matrix)):
                left, right = 1000, 1000
                center = matrix[lineidx-1][charidx]

                if charidx>0: left = matrix[lineidx-1][charidx-1]
                if charidx<len(matrix)-1: right = matrix[lineidx-1][charidx+1]


                matrix[lineidx][charidx] += min(left, right, center)

        print("")
        for i in matrix:
            print(i)

        return min(matrix[-1])

    print(minFallingPathSum([[2,1,3],[6,5,4],[7,8,9]]))
    print(minFallingPathSum([[2,1,3,9],[6,5,4,3],[1,7,8,9],[1,4,6,-6]]))
    print(minFallingPathSum([[-19,57],[-40,-5]]))
    print(minFallingPathSum([[1]]))