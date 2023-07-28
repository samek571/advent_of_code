import collections


class Solution:
    def snakesAndLadders(self, board) -> int:
        '''rearange matrix by iterating bacwards and reversing each odd line, making one long-ass list'''
        nboard = [] ; n = len(board)
        for i in range(n - 1, -1, -1):
            if i % 2 != n % 2:
                for j in range(n):
                    nboard.append(board[i][j])
            else:
                for j in range(n - 1, -1, -1):
                    nboard.append(board[i][j])
    
    
        '''apply bfs - since we want to know the shortest path - on the new matrix, 
        we hold visited'''

        visited = {1} ; q = collections.deque([(1, 0)])
        while q:
            curr = q.popleft()

            '''if its still in the board we want to take each position that is within the range of a roll dice'''
            for roll in range(6):
                new = nboard[curr[0] + roll]

                if curr[0] + roll <= n*n and nboard[curr[0] + roll] == -1:
                    new = curr[0] + roll + 1

                if new not in visited:
                    visited.add(new)

                    if new == n * n: return curr[1] + 1

                    q.append((new, curr[1] + 1))


        return -1


def main():
    sol = Solution()
    print(sol.snakesAndLadders([[-1,-1],[-1,3]]))
    print(sol.snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
    print(sol.snakesAndLadders([[-1,-1,30,14,15,-1],[23,9,-1,-1,-1,9],[12,5,7,24,-1,30],[10,-1,-1,-1,25,17],[32,-1,28,-1,-1,32],[-1,-1,23,-1,13,19]]))
    print(sol.snakesAndLadders([[-1,1,2,-1],[2,13,15,-1],[-1,10,-1,-1],[-1,6,2,8]]))

if __name__ == "__main__": main()
