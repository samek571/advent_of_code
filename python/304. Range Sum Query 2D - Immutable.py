class NumMatrix:
    def __init__(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if i==0 and j==0: continue
                elif i==0: matrix[i][j] += matrix[i][j-1]
                elif j==0: matrix[i][j] += matrix[i-1][j]
                else: matrix[i][j] += matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]

        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = b = c = d = 0
        a = self.matrix[row2][col2]
        if row1>0 and col1>0: b = self.matrix[row1-1][col1-1]
        if row1>0: c = self.matrix[row1-1][col2]
        if col1>0: d = self.matrix[row2][col1-1]

        return (a+b) - (c+d)