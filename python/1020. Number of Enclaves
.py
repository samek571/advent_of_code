class Solution:
    
    def dfs(self, i: int, j: int, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1: return

        grid[i][j] = 0 ; dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            self.dfs(nx, ny, grid)


    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if (i*j==0 or i==m-1 or j==n-1) and (grid[i][j]==1):
                    self.dfs(i, j, grid)

        cnt = 0
        for line in grid:
            cnt += line.count(1)

        return cnt
