class Solution:
    def findBall(self, grid):

        outpout, r, c = [], len(grid), len(grid[0])

        def dfs(x, y):
            if x >= r: return y

            if grid[x][y] == 1:
                if 0<=y+1<c and grid[x][y+1] == 1:
                    return dfs(x+1, y+1)

                else: return -1

            else: 
                if 0<=y-1<c and grid[x][y-1] == -1:
                    return dfs(x+1, y-1)

                else: return -1



        for y in range(c):
            outpout.append(dfs(0, y))

        return outpout


def main():
    sol = Solution()
    print(sol.findBall([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]))
    print(sol.findBall([[-1]]))
    print(sol.findBall([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]))

if __name__ == "__main__": main()