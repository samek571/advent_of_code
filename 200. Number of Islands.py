class Solution:
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1': return
        grid[i][j] = "5"
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)


    def numIslands(self, grid) -> int:
        C = len(grid)
        R = len(grid[0])

        cnt=0
        for x in range(C):
            for y in range(R):
                if grid[x][y] == "1":
                    self.dfs(grid, x, y)
                    cnt+=1

        return cnt


def main():
    sol = Solution()
    print(sol.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))
    print(sol.numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))

if __name__ == "__main__": main()