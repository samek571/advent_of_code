class Solution:
    def spiralOrder(matrix):

        output=[]
        while len(matrix[0])>=3 and len(matrix)>=3:
            #to the right
            for i in matrix[0]:
                output.append(i)

            #down
            for i in range(1,len(matrix)-1):
                output.append(matrix[i][-1])
                matrix[i].remove((matrix[i][-1]))

            #left
            for i in range(len(matrix[-1]), 0, -1):
                output.append(matrix[-1][i-1])

            #up
            k = 2
            while k != len(matrix):
                output.append(matrix[-k][0])
                matrix[-k].remove(matrix[-k][0])
                k += 1

            matrix.remove(matrix[0])
            matrix.remove(matrix[-1])

        # ++++++++++++
        if len(matrix)==1:
            for i in matrix[0]:
                output.append(i)
        # +
        # +
        # +
        elif len(matrix[0])==1:
            for i in matrix:
                output.append(i[0])

        # ++++++++++
        # ++++++++++
        elif len(matrix)==2:
            for i in matrix[0]:
                output.append(i)
            for i in range(len(matrix[-1]), 0, -1):
                output.append(matrix[-1][i-1])
            return output

        # ++
        # ++
        # ++
        else:
            for i in matrix[0]:
                output.append(i)
            matrix.remove(matrix[0])

            for i in range(len(matrix)):
                output.append(matrix[i][-1])
                matrix[i].remove(matrix[i][-1])

            matrix.reverse()
            for i in matrix:
                output.append(i[0])

        return output

    print(spiralOrder([[1,2],[3,4],[5,6],[7,8]]))   #[1, 2, 4, 6, 8, 7, 5, 3]
    print(spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))  #[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16,17,18]]))   #[1, 2, 3, 6, 9, 12, 15, 18, 17, 16, 13, 10, 7, 4, 5, 8, 11, 14]
    print(spiralOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))#[1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
    print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))   #[1, 2, 3, 6, 9, 8, 7, 4, 5]
    print(spiralOrder([[1, 2, 3], [4, 5, 6]]))      #[1, 2, 3, 6, 5, 4]
