import collections

class Solution:
    def allPathsSourceTarget(self, matrix):# -> List[List[int]]:

        o, n = [], len(matrix)
        q = collections.deque()
        q.append([0])

        while q:
            path = q.popleft()
            if path[-1] == n-1:
                o.append(path)
                continue

            for new in matrix[path[-1]]:
                q.append(path+[new])


        return o



def main():
    sol = Solution()
    print(sol.allPathsSourceTarget([[1,2],[3],[3],[]]))
    print(sol.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
    print(sol.allPathsSourceTarget([[1],[]]))

if __name__ == "__main__": main()
