#prefix sum clearly
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # n, m = len(matrix), len(matrix[0])
        # ps = [[0 for j in range(m)] for i in range(n)]

        # for i in range(n):
        #     for j in range(m):
        #         if j == 0:
        #             ps[i][j] = matrix[i][j]
        #         else:
        #             ps[i][j] = ps[i][j-1] + matrix[i][j]

        # self.ps = ps
        self.ps = [([0] + list(accumulate(matrix[i]))) for i in range(len(matrix))]



    def update(self, row: int, col: int, val: int) -> None:
        diff = val - (self.ps[row][col+1] - self.ps[row][col]) 

        for i in range(col+1, len(self.ps[row])):
            self.ps[row][i] = self.ps[row][i] + diff


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for row in range(row1, row2+1):
            res += self.ps[row][col2+1] - self.ps[row][col1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
