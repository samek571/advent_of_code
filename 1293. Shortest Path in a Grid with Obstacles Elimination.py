class Solution:
    '''it has to be treated as normal bfs just once k gets sub 0 the path is definitely invalid'''
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = set()
        queue = collections.deque([(0, 0, 0, k)])

        #we can walk manhattan distance freely
        if k > (len(grid)-1 + len(grid[0])-1):
            return len(grid)-1 + len(grid[0])-1

        #bfs
        while queue:
            row, col, steps, remaining_k = queue.popleft()

            #satisfying condition
            if row == rows - 1 and col == cols - 1:
                return steps

            #next step
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + dr, col + dc

                #some might be invalid
                if 0 <= new_row < rows and 0 <= new_col < cols:
                    
                    if grid[new_row][new_col] == 0 and (new_row, new_col, remaining_k) not in visited:
                        visited.add((new_row, new_col, remaining_k))
                        queue.append((new_row, new_col, steps + 1, remaining_k))

                    if grid[new_row][new_col] == 1 and remaining_k > 0 and (new_row, new_col, remaining_k-1) not in visited:
                        visited.add((new_row, new_col, remaining_k-1))
                        queue.append((new_row, new_col, steps + 1, remaining_k-1))

        return -1
