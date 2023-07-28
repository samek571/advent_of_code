class Solution:
    #by storing offers in a pq each action is pre-defined;

    '''
    - lets say offer is a (profit[i], capital[i]) and we have an array of them sorted by capital req and keep and we track of our capital
    - each and everytime after we finish offer there has to be replanage of other available jobs which will be kept in pq
    - since each is done in O(1) meaning we are capped just by the amount of offers which means we go as follows but dont quite finish the problem.
    '''

    # i have my doubts whether or not it is worthy to make deque, it could be solved by an iterator most likely
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        allOffers = collections.deque(sorted([(capital[i], profits[i]) for i in range(len(capital))], key=lambda x: (x[0], x[1])))

        availableOffers=[] ; heapq.heapify(availableOffers)
        while k:
            k-=1

            while allOffers and allOffers[0][0] <= w:
                curr = allOffers.popleft()
                heapq.heappush(availableOffers, -curr[1])
            
            #we have time to do IPO but there is nothing on the market
            if not availableOffers: break
            #since we have done min heap by sorting its values in minus
            w -= heapq.heappop(availableOffers)
        
        return w


