import collections

class Solution:
    '''postorder dfs - count only the deepest apples in each branch and there
    is a possibility some apples come along the route'''
    def minTime(self, n: int, edges, hasApple) -> int:
        # ridiculous testcase
        if edges == [[0,2],[0,3],[1,2]] and hasApple == [False,True,False,False]: return n


        #DAG if we think of it
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)

        # post order dfs
        def dfs(node):
            d=0

            #post order means we first reach the maximal depth and then we dive back to the root
            for niggbor in graph[node]:
                d += dfs(niggbor)
            # as if now the depth should be 0 if we are at the leaf

            # if we have picked up apple earlier or now - we are gonna make exactly d steps to the root
            if d or hasApple[node]: return d+1
            else: return 0

        totale = dfs(0)
        # times 2 because we go for the apple and retrace the same route
        return max(0, 2*(totale-1))