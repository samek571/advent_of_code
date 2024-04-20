class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        
        def dfs(curr,par,dist,hmap,seen):
            nonlocal ans
            if curr in hmap and hmap[curr][1] == 1:
                ans = min(ans,dist - hmap[curr][0])
                return
            
            seen.add(curr)
            hmap[curr] = [dist,1]
            for it in graph[curr]:
                if it != par and (it not in hmap or hmap[it][0] > dist + 1 or hmap[it][1] == 1):
                    dfs(it,curr,dist+1,hmap,seen)
            
            hmap[curr] = [dist,0]
            seen.remove(curr)
            return
        

        seen = set() ; ans = float('inf')
        for i in range(n):
            if i not in seen:
                hmap = collections.defaultdict(list)
                dfs(i,-1,0,hmap,seen)  

        return ans if ans != float('inf') else -1




'''
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:

        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        
        
        #going straight to the nothing and once we step in the same shit twice, we look at the lenght of the cycle
        def dfs(node, prev, path, length, depth):
            nonlocal ans
            
            if node in path:
                cycle = length - path.index(node) + 1
                ans = min(ans, cycle)
                return
            
            if depth == 0: return
            
            for neighbor in graph[node]:
                if neighbor == prev: continue
                
                dfs(neighbor, node, path + [node], length+1, depth-1)



        seen = set() ; ans = float('inf') ; memo = {}
        for node in range(n):
            
            #only then we can talk --> O(v+e)
            if node not in seen:
                dfs(node, None, [], 0, n)
        
        if ans == float('inf'): return -1
        else: return ans
'''
