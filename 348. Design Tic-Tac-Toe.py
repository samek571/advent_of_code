class TicTacToe:

    # we simply just store number of X and O in the list, no need to note each notation --> O(4n+2)
    # once the list is full only then we can confidently claim a winned - if any
    def __init__(self, n: int):
        self.lines = {i:[0,0] for i in range(n)}
        self.cols = {i:[0,0] for i in range(n)}
        self.diag = {0:[0,0], 1:[0,0]}
        self.n = n


    def move(self, row: int, col: int, player: int) -> int:
        player-=1
        
        #diagonals, doing 2 ifs because the mid of mid shall be counted to both
        if row == col:
            self.diag[0][player] +=1
            if self.diag[0][player] == self.n:
                return player+1

        if row == self.n - 1 - col:
            self.diag[1][player] +=1
            if self.diag[1][player] == self.n:
                return player+1
                


        self.lines[row][player]+=1
        if self.lines[row][player] == self.n:
            return player+1
        
        self.cols[col][player]+=1
        if self.cols[col][player] == self.n:
            return player+1
        
        return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
