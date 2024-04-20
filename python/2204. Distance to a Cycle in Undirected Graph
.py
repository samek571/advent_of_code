'''i kinda understand why is it hard labeled but the logic is pretty simple and should be medium'''

class Solution:
    def __init__(self):
        self.graph = None
        self.cycle = None
        self.inCycle = set()
    
    
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        #booting the graph
        self.graph = collections.defaultdict(list)
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])



        visited = {}
        cycle_nodes = set()

        def dfs(node, prev, seq_no):
            if len(cycle_nodes):
                return

            visited[node] = seq_no
            for nei in self.graph[node]:
                if nei != prev:
                    if nei in visited:
                        # back edge detected
                        # find the index of nei in visited_list
                        idx = visited[nei]
                        # gather all the nodes with seq_no>= idx in visited map
                        for key, value in visited.items():
                            if value >= idx:
                                cycle_nodes.add(key)
                        return
                    else:
                        dfs(nei, node, seq_no+1)
            del visited[node]

        dfs(0, None, 1)


        self.cycle = cycle_nodes
        #global banned vertices since "cycles" are going to me a q in bfs
        for v in self.cycle:
            self.inCycle.add(v)
        
        #forming the output array
        ret = [-1] * n
        self.bfs(ret)
        
        return ret
    


    #bfs done by levels, starting with all the cycle vertices
    def bfs(self, ret):
        queue = collections.deque(self.cycle)
        distance = 0
        while queue:
            #the level passage
            for _ in range(len(queue)):
                vertex = queue.popleft()
                ret[vertex] = distance
                
                for neighbor in self.graph[vertex]:
                    if neighbor not in self.inCycle:
                        self.inCycle.add(neighbor)
                        queue.append(neighbor)
            distance += 1
