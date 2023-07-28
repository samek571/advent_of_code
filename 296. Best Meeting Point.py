class Solution:
    def minTotalDistance(self, grid) -> int:

        ex, ey= [], []

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    ex.append(x)
                    ey.append(y)

        ey, ex = sorted(ey), sorted(ex)
        xmed, ymed, cumulative_distance = ey[len(ey)//2], ex[len(ex)//2], 0

        for i in range(len(ey)):
            cumulative_distance += abs(ey[i] -xmed)
            cumulative_distance += abs(ex[i] -ymed)

        return cumulative_distance

def main():
    sol = Solution()
    print(sol.minTotalDistance([[1,0,0,0,1],[0,0,0,0,0],[0,0,1,0,0]]))
    print(sol.minTotalDistance([[1,1]]))

if __name__ == "__main__": main()

