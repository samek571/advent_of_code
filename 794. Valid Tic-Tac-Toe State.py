class Solution:
    def validTicTacToe(mat) -> bool:


        mapping = {"X":1, " ":0, "O":-1}
        board= [mapping[i] for i in "".join(mat)] # compressing to 1D since 2D is unecesarry
        total = sum(board)

        #their count can be shifted by 1 at most because they take turns
        if total >> 1: return False

        #O wins if there is 1
        n = -3 if total == 1 else 3
        #little bit ugly but the prettiest it can get probably
        #all the winning 3matches sum up to some number and if there is -3 or 3 it means we have a win
        if n in {board[0]+board[1]+board[2], board[3]+board[4]+board[5], board[6]+board[7]+board[8],
                 board[0]+board[3]+board[6], board[1]+board[4]+board[7], board[2]+board[5]+board[8],
                 board[0]+board[4]+board[8], board[2]+board[4]+board[6]}: return False

        return True


    print(validTicTacToe(["OOO","   ","   "]))  #false
    print(validTicTacToe(["OOO","XX ","   "]))  #false
    print(validTicTacToe(["OOO","XX ","X  "]))  #true
    print(validTicTacToe(["OOO","XX ","XX "]))  #true

    print(validTicTacToe(["XOX"," X ","   "]))  #false
    print(validTicTacToe(["O  ","   ","   "]))  #false
    print(validTicTacToe([" X ","   ","   "]))  #true
    print(validTicTacToe(["XXX","   ","OOO"]))  #false
    print(validTicTacToe(["XOX","O O","XOX"]))  #true


# class Solution:
#     def validTicTacToe(board):
#         number_of_x=0
#         number_of_o=0
#
#         for i in board:
#             for bullshit in i:
#                 if bullshit == "O": number_of_o+=1
#                 elif bullshit == "X": number_of_x+=1
#
#         #taking care of abnormal amount of xs and os
#         if number_of_o>number_of_x or number_of_x-number_of_o>=2: return False
#
#         #if Os win then it has to be exactly the same amount of xs and not being in the winning position
#         if number_of_o<=number_of_x and number_of_o>=3 and (
#
#             (board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O") or\
#             (board[2][0]=="O" and board[1][1]=="O" and board[0][2]=="O") or\
#
#             (board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="O") or \
#             (board[1][0]=="O" and board[1][1]=="O" and board[1][2]=="O") or \
#             (board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="O") or\
#
#             (board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="O") or \
#             (board[0][1]=="O" and board[1][1]=="O" and board[2][1]=="O") or\
#             (board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O") \
#  \
#                 ) and not ( \
#
#             (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or \
#             (board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X") or \
#  \
#             (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or \
#             (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or \
#             (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") or \
#  \
#             (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") or \
#             (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") or \
#             (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X") \
#                 ): return True
#
#         elif number_of_x>number_of_o and number_of_x>=3 and (
#
#         (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or \
#         (board[2][0] == "X" and board[1][1] == "X" and board[0][2] == "X") or \
# \
#         (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or \
#         (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or \
#         (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") or \
# \
#         (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") or \
#         (board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X") or \
#         (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X") \
# \
#             ) and not ( \
#
#         (board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O") or\
#         (board[2][0]=="O" and board[1][1]=="O" and board[0][2]=="O") or\
#
#         (board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="O") or \
#         (board[1][0]=="O" and board[1][1]=="O" and board[1][2]=="O") or \
#         (board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="O") or\
#
#         (board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="O") or \
#         (board[0][1]=="O" and board[1][1]=="O" and board[2][1]=="O") or\
#         (board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O") \
#             ): return True
#
#         return True
#
#     print(validTicTacToe(["OOO","   ","   "]))  #false
#     print(validTicTacToe(["OOO","XX ","   "]))  #false
#     print(validTicTacToe(["OOO","XX ","X  "]))  #true
#     print(validTicTacToe(["OOO","XX ","XX "]))  #true
#
#     print(validTicTacToe(["XOX"," X ","   "]))  #false
#     print(validTicTacToe(["O  ","   ","   "]))  #false
#     print(validTicTacToe([" X ","   ","   "]))  #true
#     print(validTicTacToe(["XXX","   ","OOO"]))  #false
#     print(validTicTacToe(["XOX","O O","XOX"]))  #true
