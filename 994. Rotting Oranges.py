import collections

class Solution:
    def orangesRotting(self, grid) -> int:
        R, C, q = len(grid), len(grid[0]), collections.deque([])
        fresh_to_go, max_depth = 0, 0

        for x in range(R):
            for y in range(C):
                if grid[x][y] == 2:
                    q.append([x,y, max_depth])
                    grid[x][y] = 1
                    fresh_to_go+=1

                elif grid[x][y] == 1:
                    fresh_to_go+=1

        while q:
            x,y,d = q.popleft()

            if 0<=x<R and 0<=y<C and grid[x][y] == 1:
                #print(x,y)
                fresh_to_go-=1
                grid[x][y]=2
                max_depth = max(max_depth, d)

                for i,j in [[1,0], [-1,0], [0,-1], [0,1]]:
                    q.append([x+i, y+j, d+1])


        return max_depth if fresh_to_go == 0 else -1



def main():
    sol = Solution()
    print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
    print(sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
    print(sol.orangesRotting([[0,2]]))
    print(sol.orangesRotting([[0,1]]))
    print(sol.orangesRotting([[0,1],[1,0]]))
    print(sol.orangesRotting([[0,1],[2,0]]))
    print(sol.orangesRotting([[0,1],[2,2]]))
    print(sol.orangesRotting([[0,1],[2,1]]))

if __name__ == "__main__": main()
