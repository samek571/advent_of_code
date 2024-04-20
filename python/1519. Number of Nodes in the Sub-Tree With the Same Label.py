import collections


class Solution:
    def countSubTrees(self, n: int, edges, labels: str):

        #boot the graph
        graph = collections.defaultdict(list)
        for x,y in edges:
            graph[x] += [y]
            graph[y] += [x]

        #innit dfs
        seen = set()
        def dfs(node):
            seen.add(node)
            c = collections.Counter(labels[node])

            # dfs further expansion
            for i in graph[node]:
                if i not in seen:
                    c += dfs(i)

            # as we dive back to root
            output[node] = c[labels[node]]
            # return c so closer to root it has all of its children included
            return c


        output = [0]*n
        dfs(0)
        return output


def main():
    sol = Solution()
    print(sol.countSubTrees(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"))
    print(sol.countSubTrees(n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"))
    print(sol.countSubTrees(n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"))

if __name__ == "__main__": main()
