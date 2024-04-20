import itertools


class Solution:
    '''all O that survive are those who touch the edges of grid or chain of neighbors is touching'''
    def solve(self, grid) -> None:
        R, C = len(grid), len(grid[0])

        def dfs(x,y):

            if 0<=x<R and 0<=y<C and grid[x][y] == "O":
                grid[x][y] = "$"
                for i,j in [[0,1], [1,0], [-1,0], [0,-1]]:
                    dfs(x+i,y+j)



        for x in range(R):
            s=''
            for y in range(C):
                s+=grid[x][y]

            print(s)
        print("")

        # survivor recursion starter
        for y in range(1, C-1):
            dfs(0,y)
            dfs(R-1, y)

        #avoid duplicated entries
        for x in range(R):
            dfs(x, 0)
            dfs(x, C-1)

        # changing bad O to X
        for i, j in itertools.product(range(R), range(C)):
            grid[i][j] = 'X' if grid[i][j] != '$' else 'O'


        for x in range(R):
            s=''
            for y in range(C):
                s+=grid[x][y]

            print(s)

        return grid


def main():
    sol = Solution()
    print(sol.solve([["O","O","O","O","X","X"],["O","O","O","O","O","O"],["O","X","O","X","O","O"],["O","X","O","O","X","O"],["O","X","O","X","O","O"],["O","X","O","O","O","O"]]))
    #print(sol.solve([["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]))
    #print(sol.solve([["X","O","X"],["O","X","O"],["X","O","X"]]))
    # print(sol.solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
    # print(sol.solve([["X"]]))
    # print(sol.solve([["O"]]))
    # print(sol.solve([["X","X","X"], ["X","O","X"], ["X","X","X"]]))
    # print(sol.solve([["X","X","X"], ["X","O","O"], ["X","X","X"]]))

if __name__ == "__main__": main()