class Solution:
    '''dijkstred bfs n+m * logn'''
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:

        q = [(0, 0, False)]
        costs = [float('inf')] * (len(express) + 1)
        visited = set()

        while q:
            #boot of the case
            cost, index, is_express = heapq.heappop(q)
            costs[index] = min(cost, costs[index])
            
			#validation
            if index == len(express) or (index, is_express) in visited: continue
            visited.add((index, is_express))
            
            #depending on which line we are at
            if is_express:
                heapq.heappush(q, (cost + express[index], index + 1, True))
                heapq.heappush(q, (cost, index, False))
            else:
                heapq.heappush(q, (cost + regular[index], index + 1, False))
                heapq.heappush(q, (cost + expressCost, index, True))
        
		#the first one just so the while cyclus runs
        return costs[1:]
