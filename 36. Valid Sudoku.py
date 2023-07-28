from collections import  defaultdict

class Solution:
    def isValidSudoku(self, board) -> bool:

        sq, row, column = defaultdict(set), defaultdict(set), defaultdict(set)

        for x in range(9):
            for y in range(9):

                curr = board[x][y]
                boxid = x//3*3+y//3

                if curr == ".": continue

                elif curr in row[x]: return False
                elif curr in column[y]: return False
                elif curr in sq[boxid]: return False

                column[y].add(curr)
                row[x].add(curr)
                sq[boxid].add(curr)

        return True


def main():
    sol = Solution()
    print(sol.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
    print(sol.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))

if __name__ == "__main__": main()