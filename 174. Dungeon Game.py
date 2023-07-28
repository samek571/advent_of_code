class Solution:
    def calculateMinimumHP(matrix) -> int:
        print("")
        for i in matrix:
            print(i)
        print("after mod")

        R, C = len(matrix), len(matrix[0])
        hp = [[0]*C for _ in range(R)]
        hp[-1][-1] = max(1, 1-matrix[-1][-1])

        for i in range(C-2, -1, -1): hp[-1][i] = max(1, hp[-1][i+1]-matrix[-1][i])
        for i in range(R-2,-1,-1): hp[i][-1] = max(1, hp[i+1][-1]-matrix[i][-1])

        for i in range(R-2,-1,-1):
            for j in range(C-2,-1,-1):
                hp[i][j] = max(1, min(hp[i+1][j]-matrix[i][j], hp[i][j+1]-matrix[i][j]))

        for i in hp:
            print(i)

        return hp[0][0]

    print(calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
    print(calculateMinimumHP([[2,-3,31],[5,-10,-3],[5,-3,-5]]))
    print(calculateMinimumHP([[0]]))
