class Solution:
    def gameOfLife(board) -> None:

        print("ini")
        for i in board:
            print(i)
        print("")

        C = len(board)
        R = len(board[0])
        
        neighbors=[[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
        for i in range(C):
            for j in range(R):

                #counting living neighbors
                number_of_ones = 0
                for n in neighbors:
                    if 0 <= i+n[0] < C and 0 <= j+n[1] < R:
                        if board[i+n[0]][j+n[1]] > 0: number_of_ones+=1

                #marking changes to not interfere with ongoing comparations
                if board[i][j] == 1:
                    if number_of_ones < 2 or number_of_ones > 3: board[i][j] = 2
                elif board[i][j] == 0:
                    if number_of_ones == 3: board[i][j] = -1

        #making everything 0 and 1
        for i in range(C):
            for j in range(R):
                if board[i][j] == -1: board[i][j] = 1
                elif board[i][j] == 2: board[i][j] = 0


        print("mody")
        for i in board:
            print(i)
        print("")

    print(gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))
    print(gameOfLife([[1,1],[1,0]]))
    print(gameOfLife([[1,0,1,1], [1,0,0,0], [1,0,0,0], [1,0,1,1]]))

        # changes = []
        # neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        #
        # for i in range(len(board)):
        #     for j in range(len(board[0])):
        #
        #         # counting living neighbors
        #         number_of_ones = 0
        #         for i in neighbors:
        #             if 0 <= i + i[0] < C and 0 <= j + i[1] < len(board[0]):
        #                 if board[i + i[0]][j + i[1]] == 1: number_of_ones += 1
        #
        #         # marking changes
        #         if board[i][j] == 1:
        #             if number_of_ones < 2 or number_of_ones > 3: changes.append([i, j])
        #         else:
        #             if number_of_ones == 3: changes.append([i, j])
        #
        # # applying changes
        # for i in changes:
        #     if board[i[0]][i[1]] == 1:
        #         board[i[0]][i[1]] = 0
        #     else:
        #         board[i[0]][i[1]] = 1
