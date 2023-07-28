class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        '''first thought - failed me because we dont necessarily sum 2 lowest by this method
        therefore it was a good idea to add a feature that inserts the sum of 2 lowest into the sorted list''' 
        # sticks.sort()
        #
        # n = len(sticks)-1
        # o=sticks[0]*n
        # for i in range(1,n+1):
        #     o+= (n*sticks[i])
        #     n-=1
        
        # return o

        heapq.heapify(sticks)
        o = 0
        while len(sticks) > 1:
            a, b = heapq.heappop(sticks), heapq.heappop(sticks)
            o+=a+b
            heapq.heappush(sticks, a+b)
        
        return o
