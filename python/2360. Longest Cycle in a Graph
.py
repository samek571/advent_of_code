class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        seen = set() ; ans = -1

        for node in range(len(edges)):
            
            #only then we can talk --> O(v+e)
            if node not in seen:
                visited = {} ; count = 0 ; q = [node]
                
                while q:
                    curr = q.pop()
                    adj = edges[curr] # the one and only neighbor
                    visited[curr] = count # ith node in the cycle
                    
                    if adj == -1 or adj in seen: continue #seen or no not connecte

                    count += 1 # we move on further one since its possible now ^^
                    if adj in visited: #end of the cycle
                        ans = max(ans,count - visited[adj])
                        continue
                    else:
                        q.append(adj) #we carry on in the cycle detection
                
                
                for i in visited:
                    seen.add(i)
        
        
        return ans 
