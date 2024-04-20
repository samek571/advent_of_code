class Solution:
    def generateMatrix(n: int):
        matrix = [[0] * n for _ in range(n)]

        print(n)

        #first row
        actual=1
        rotation=90
        i,j=0,0
        while actual <= n**2:

            if rotation == 90:
                while 0<= j <n and matrix[i][j] == 0:
                    matrix[i][j]=actual
                    j+=1
                    actual+=1

                rotation +=90
                j-=1
                i+=1

            if rotation == 180:
                while  0<= i <n and matrix[i][j] == 0:
                    matrix[i][j] = actual
                    i += 1
                    actual += 1

                rotation += 90
                i-=1
                j-=1

            if rotation == 270:
                while 0<= j <n and matrix[i][j] == 0:
                    matrix[i][j]=actual
                    j-=1
                    actual+=1

                rotation = 0
                j+=1
                i-=1

            if rotation == 0:
                while  0<= i <n and matrix[i][j] == 0:
                    matrix[i][j] = actual
                    i -= 1
                    actual += 1

                rotation += 90
                i+=1
                j+=1

        # for u in matrix:
        #     print(u)
        # print("")
        return matrix

    print(generateMatrix(5))
    print(generateMatrix(3))
    print(generateMatrix(4))
    print(generateMatrix(6))
    print(generateMatrix(10))
    print(generateMatrix(1))
    print(generateMatrix(2))
