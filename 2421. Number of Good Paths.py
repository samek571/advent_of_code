class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        edges.sort(key=lambda x: max(vals[x[0]], vals[x[1]]))
        n = len(vals)
        parents = list(range(n)); size = [1]*n
        
        def find(i): 
            if parents[i] != i:
                parents[i] = find(parents[i])
            return parents[i]        
        
        goodPaths = n
        for a,b in edges:
            parent_a, parent_b = find(a), find(b)            
            
            if vals[parent_a] == vals[parent_b]:
                goodPaths += size[parent_a] * size[parent_b]
                parents[parent_a] = parent_b
                size[parent_b] += size[parent_a]
            
            elif vals[parent_a] > vals[parent_b]:
                parents[parent_b] = parent_a
            
            else:
                parents[parent_a] = parent_b
        
        
        return goodPaths




        # #graph boot
        # graph = collections.defaultdict(set)
        # for a,b in edges:
        #     graph[a].add(b)
        #     graph[b].add(a)

        # total=len(vals)
        # visit=[0]*total
        # self.result=0
        

        # def DFS(node):
        #     #to not being stuck in a loop
        #     visit[node]=1

        #     self.result+=1
        #     counter = collections.Counter([vals[node]])
        #     for nei in graph[node]:
        #         if not visit[nei]: 
        #             for item,freq in DFS(nei).items():
                        
        #                 # we have fount a good path
        #                 # just there can be a lot of partitions of it -> by finding one we dont end since there might be another one
        #                 if item>=vals[node]:
        #                     self.result+=counter[item]*freq
        #                     counter[item]+=freq
        #     return counter
        
        # #starting dfs from the leaf since in binary tree like this vertices with bigger values are deeper
        # DFS(total-1)
        # return self.result
