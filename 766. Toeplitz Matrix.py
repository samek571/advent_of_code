class Solution:
    def isToeplitzMatrix(self, matrix):

        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])-1):
                if matrix[i][j+1] != matrix[i-1][j]: return False
        return True



def main():
    sol = Solution()
    print(sol.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
    print(sol.isToeplitzMatrix([[1,2],[2,2]]))

if __name__ == "__main__": main()