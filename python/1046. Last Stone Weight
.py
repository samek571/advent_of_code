class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:        
        p=[]
        heapq.heapify(p)
        for stone in stones:
            heapq.heappush(p,-stone)
        
        
        while len(p)>1:
            f=-heapq.heappop(p)
            s=-heapq.heappop(p)
            
            if f==s: continue
            else: heapq.heappush(p,-(f-s))
        
        
        return -heapq.heappop(p) if p else 0
