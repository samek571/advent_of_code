class Solution:
    def setZeroes(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        print("ini")
        for i in matrix:
            print(i)
        print("")

        is_col=False
        #modifying
        for lineidx in range(len(matrix)):
            if matrix[lineidx][0] == 0: is_col=True

            for charidx in range(1, len(matrix[0])):
                if matrix[lineidx][charidx] == 0:
                    matrix[lineidx][0] = 0
                    matrix[0][charidx] = 0

        print("mody")
        for i in matrix:
            print(i)
        print("")


        #columns and rows
        for lineidx in range(1, len(matrix)):
            for charidx in range(1, len(matrix[0])):
                if not matrix[lineidx][0] or not matrix[0][charidx]:
                    matrix[lineidx][charidx] = 0


        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0

        if is_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0


        for i in matrix:
            print(i)
        print("\nnew:")

    print(setZeroes([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]))

    print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
    print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
    print("####################")
    print(setZeroes([[0,1,2,0],[3,0,5,2],[1,3,1,5]]))
    print(setZeroes([[0]]))
    print(setZeroes([[1]]))
    print(setZeroes([[1,0],[1,1]]))
    print(setZeroes([[0],[1]]))
    print(setZeroes([[1],[0]]))
