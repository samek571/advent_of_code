class Solution:
    def maximalSquare(matrix) -> int:
        print("")
        for i in matrix:
            print(i)
        print("after mod")

        R, C = len(matrix), len(matrix[0])
        new = [[0]*C for _ in range(R)]

        #handling edges
        new[0][0] = int(matrix[0][0])
        totalmax=new[0][0]
        for i in range(1, C):
            new[0][i] = int(matrix[0][i])
            totalmax = max(totalmax, new[0][i])
        for i in range(1, R):
            new[i][0] = int(matrix[i][0])
            totalmax = max(totalmax, new[i][0])

        #handling rest
        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][j] == "1":
                    new[i][j] = min(int(new[i-1][j-1]),int(new[i][j-1]), int(new[i-1][j]))+1
                    totalmax = max(totalmax, new[i][j])
                else: new[i][j]=0


        for i in new:
            print(i)

        return totalmax**2

    print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    print(maximalSquare([["0","1"], ["1","0"]]))
    print(maximalSquare([["0","0"], ["0","0"]]))
    print(maximalSquare([["1","1"], ["1","1"]]))
    print(maximalSquare([["0","1"]]))
    print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))