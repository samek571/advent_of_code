from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        lenght = len(grid)

        if lenght == 1: return 1 if grid[0][0]==0 else -1
        if grid[lenght-1][lenght-1] == 1 or grid[0][0] == 1: return -1


        visited_matrix = [[0 for _ in range(lenght)] for _ in range(lenght)]
        queue = deque()
        queue.append([0,0,1])

        while queue:
            x,y, lvl = queue.popleft()

            if any([x<0, y<0, x>=lenght, y>=lenght]): continue
            if any([visited_matrix[x][y] == 1, grid[x][y]==1]): continue

            if x == lenght-1 and y == lenght-1: 
                return lvl

            visited_matrix[x][y] = 1

            for i in range(x-1, x+2):
                for j in range(y-1, y+2):
                    queue.append([i,j, lvl+1])

        return -1



def main():
    sol = Solution()
    print(sol.shortestPathBinaryMatrix([[0,1],[1,0]]))
    print(sol.shortestPathBinaryMatrix([[0,1,1], [1,0,1], [1,1,0]]))
    print("#################")
    print(sol.shortestPathBinaryMatrix([[1]]))
    print(sol.shortestPathBinaryMatrix([[0]]))

if __name__ == "__main__": main()
