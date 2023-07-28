class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        
        def helper(r, c, total, visited):
            nonlocal maxx
            if r < 0 or r >= rows or c < 0 or c >= cols or\
                grid[r][c] == 0 or (r, c) in visited:
                return
            
            total += grid[r][c]
            maxx = max(maxx, total)
            
            visited.add((r, c))
            helper(r + 1, c, total, visited)
            helper(r - 1, c, total, visited)
            helper(r, c + 1, total, visited)
            helper(r, c - 1, total, visited)
            visited.remove((r, c)) 
        

        rows = len(grid) ; cols = len(grid[0])
        greatest = 0 ; starts = []
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != 0:
                    maxx = 0
                    helper(row, col, 0, set())
                    greatest = max(maxx, greatest)
                    
        return greatest
