class Solution:
    def wallsAndGates(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        rows = len(grid) ; cols = len(grid[0]) ; queue = collections.deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))


        while queue:
            x, y = queue.popleft()

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != -1 and grid[nx][ny] == 2**31 - 1:
                    grid[nx][ny] = grid[x][y] + 1
                    queue.append((nx, ny))
