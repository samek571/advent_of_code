class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        q = collections.deque()

        # Adding all the land cells to the queue
        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 1:
                    q.append((row, col))

        # If all the cells are land cells or there are no water cells
        if not q or ROW * COL == len(q):
            return -1

        ret = -1
        # Perform BFS from the land cells
        while q:
            row, col = q.popleft()
            for r, c in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:
                if 0 <= r < ROW and 0 <= c < COL and grid[r][c] == 0:
                    grid[r][c] = grid[row][col] + 1
                    ret = max(ret, grid[r][c])
                    q.append((r, c))

        return ret-1
