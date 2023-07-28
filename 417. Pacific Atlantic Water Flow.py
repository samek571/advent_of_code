class Solution:
    def fx(self, matrix):
        R,C = len(matrix), len(matrix[0])
        pacific, atlantic = set(), set()

        def dfs(x,y,seen,prev):
            if 0<=x<R and 0<=y<C and (x,y) not in seen and matrix[x][y]>=prev:
                seen.add((x,y))

                for i,j in [[1,0],[-1,0],[0,-1],[0,1]]:
                    dfs(x+i,y+j,seen,matrix[x][y])

            else: return


        for r in range(R):
            dfs(r, 0, atlantic, matrix[r][0])
            dfs(r, C-1, pacific, matrix[r][C-1])

        for c in range(C):
            dfs(0, c, atlantic, matrix[0][c])
            dfs(R-1, c, pacific, matrix[R-1][c])


        return pacific & atlantic
        #return [list(h) for h in pacific & atlantic]


def main():
    sol = Solution()
    print(sol.fx([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
    print(sol.fx([[1]]))

if __name__ == "__main__": main()