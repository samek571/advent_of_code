def minPathSum(matrix) -> int:
    print("")
    for i in matrix:
        print(i)
    print("after mod")
    R, C = len(matrix) ,len(matrix[0])

    for i in range(1, C): matrix[0][i] += matrix[0][i-1]
    for i in range(1, R): matrix[i][0] += matrix[i-1][0]

    for i in range(1, R):
        for j in range(1, C):
            matrix[i][j] += min(matrix[i-1][j] , matrix[i][j-1])


    for i in matrix:
        print(i)
    return matrix[-1][-1]

print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
print(minPathSum([[1,2,3],[4,5,6]]))