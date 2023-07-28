class Solution:
    ''' post order dfs and store the longer from 2 child paths, 
    in the end  we get 2 longest paths and they are basically result'''
    def longestPath(self, parent: List[int], s: str) -> int:
        adjMat = defaultdict(list)

        for node, parent in enumerate(parent):
            if node != 0:
                adjMat[parent].append(node)
        
        sol = 0

        def solve(node):
            maxi = secMaxi = 0

            for nei in adjMat[node]:
                x = solve(nei)

                if s[nei] != s[node]:
                    if x > maxi: secMaxi, maxi = maxi, x
                    elif x > secMaxi: secMaxi = x
            
            nonlocal sol
            sol = max(sol, 1 + maxi + secMaxi)
            return maxi + 1
        
        solve(0)
        return sol
