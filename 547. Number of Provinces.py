import collections
import scipy.sparse

class Solution:
    def findCircleNum(self, matrix):# List[List[int]]) -> int:

        # shit
        # hsh = collections.defaultdict(list)
        #
        # for idx, connection in enumerate(matrix):
        #     for numidx, num in enumerate(matrix[idx]):
        #         if numidx != idx and num == 1:
        #             hsh[idx].append(numidx)

        #return scipy.sparse.csgraph.connected_components(matrix)[0]

        N = len(matrix)
        path = []

        def dfs(matrix,node,path=[]):
            for neighbor, value in enumerate(matrix[node]):
                if value and neighbor not in path:
                    path += [node]
                    path = dfs(matrix,neighbor,path)
            return path

        ans = 0
        for i in range(N):
            if i not in path:
                path = dfs(matrix,i)
                ans += 1
        return ans


def main():
    sol = Solution()
    print(sol.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
    print(sol.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]))

if __name__ == "__main__": main()