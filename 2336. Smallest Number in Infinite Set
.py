
#the way it is supposed to be done is each and everytime we have empty pq there is gonna be next greater elemnt added and it is always possible because we are poppingfrom left
class SmallestInfiniteSet:

    def __init__(self):
        self.pq = [1]
        heapq.heapify(self.pq)
        

    def popSmallest(self) -> int:
        num=heapq.heappop(self.pq)
        
        if not self.pq:
            heapq.heappush(self.pq, num+1)
        
        return num
        

    def addBack(self, num: int) -> None:
        top = max(self.pq)
        if num < top and num not in self.pq:
            heapq.heappush(self.pq, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
