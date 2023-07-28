class Solution:
    def exist(self, matrix, s: str) -> bool:
        R, C = len(matrix), len(matrix[0])
        settage = set()

        def dfs(x, y, word):

            if len(word) == 0: return True


            # for ele in [(0,1), (1,0), (-1,0), (0, -1)]:
            #     i,j = ele
            #
            #     if ((x+i,y+j) not in settage) and (0<=x+i<R and 0<=y+j<C) and (matrix[x][y] == word[0]):
            #         settage.add((x+i,y+j))
            #         dfs(x+i,y+j, word[1:])
            #         settage.remove((x+i,y+j))
            #
            #     else: return False

            #if ((x, y) in settage) or (0 > x or x >= R or 0 > y or y>= C) or (matrix[x][y] != word[0]): return False

            if (x, y) in settage: return False
            if x < 0 or y < 0 or x == R or y == C: return False
            if matrix[x][y] != word[0]: return False


            settage.add((x, y))

            res = dfs(x + 1, y, word[1:]) \
                  or dfs(x - 1, y, word[1:]) \
                  or dfs(x, y + 1, word[1:]) \
                  or dfs(x, y - 1, word[1:])

            settage.remove((x, y))
            return res




        for x in range(R):
            for y in range(C):
               if dfs(x, y, s): return True

        return False

def main():
    sol = Solution()
    print(sol.exist([["A","B","y","E"],["S","F","y","S"],["A","D","E","E"]], s = "ABCCED"))
    print(sol.exist([["A","B","y","E"],["S","F","y","S"],["A","D","E","E"]], s = "SEE"))
    print(sol.exist([["A","B","y","E"],["S","F","y","S"],["A","D","E","E"]], s = "ABCB"))

if __name__ == "__main__": main()