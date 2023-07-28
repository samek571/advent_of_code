class Solution:
    def rotate(matrix):

        size = len(matrix)
        for i in range(size):
            for j in range(i+1, size):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        for r in range(size):
            matrix[r] = matrix[r][::-1]

        for i in matrix:
            print(i)

    print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
    print(rotate([[1]]))
    print(rotate([[1,2],[3,4]]))
    print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))