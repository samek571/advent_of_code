class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        totalmax=0
        for line in range(len(grid)):
            for char in range(len(grid[0])):
                if grid[line][char] == 1:
                    totalmax = max(totalmax, self.recurection(grid, line, char))
        return totalmax

    def recurection(self, grid, line, char):
        if not(0<=line<len(grid) and 0<=char<len(grid[0])) or  0==grid[line][char]: return 0

        grid[line][char] = 0
        return 1 + self.recurection(grid, line - 1, char) + self.recurection(grid, line, char - 1) + self.recurection(grid, line, char + 1) + self.recurection(grid, line + 1, char)


def main():
    sol = Solution()
    print(sol.maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
    print(sol.maxAreaOfIsland(grid = [[0,0,0,0,0,0,0,0]]))
    print(sol.maxAreaOfIsland(grid = [[0]]))
    print(sol.maxAreaOfIsland(grid = [[1]]))

if __name__ == "__main__": main()