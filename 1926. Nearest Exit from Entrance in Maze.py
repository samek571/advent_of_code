import collections

class Solution:
    def nearestExit(self, matrix, entrance) -> int:
        x,y = entrance
        R, C = len(matrix), len(matrix[0])

        # from starting point we spill the bucket of water and the first out of border gets returned
        # each tile we visit has to be converted to "+" so we end the cycling

        matrix[x][y] = "+"
        q = collections.deque()
        q.appendleft((x,y, 0))

        while q:
            i,j, cum = q.pop()

            for r,c in [[i,j+1], [i, j-1], [i+1,j], [i-1,j]]:

                if 0<=r<R and 0<=c<C and matrix[r][c] == ".":

                    if (r==0) | (c==0) | (r==R-1) | (c==C-1):
                        return cum+1

                    matrix[r][c] = "+"
                    q.appendleft((r,c, cum+1))

        #we havent found shit
        return -1




def main():
    sol = Solution()
    print(sol.nearestExit([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]))
    print(sol.nearestExit([["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]))
    print(sol.nearestExit([[".","+"]], entrance = [0,0]))

if __name__ == "__main__": main()