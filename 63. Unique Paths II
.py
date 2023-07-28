class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            #exit
            if i >= m or j >= n or obstacleGrid[i][j] == 1:
                return 0
            #good exit
            if i == m - 1 and j == n - 1:
                return 1

            #finding exit
            down_paths = dfs(i + 1, j)
            right_paths = dfs(i, j + 1)

            #ticket to exit
            return down_paths + right_paths
        

        return dfs(0, 0)
