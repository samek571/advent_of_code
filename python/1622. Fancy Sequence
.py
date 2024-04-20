'''
lets hold a heapq in which we push (index,action) and to make it even faster it is going to be all cumulated -> prefix sum
additionally we make a hashmap to store number:index (and one index variable ofc)

since we can not delete; for each getindex query we look up the index in the heapq and return in logn 
'''

class Fancy:
    def __init__(self):
        self.arr, self.addPrefix, self.multPrefix = [], [0], [1]


    def append(self, val: int) -> None:
        self.arr.append(val)
        self.addPrefix.append(self.addPrefix[-1])
        self.multPrefix.append(self.multPrefix[-1])


    def addAll(self, inc: int) -> None:
        self.addPrefix[-1] += inc


    def multAll(self, m: int) -> None:
        self.addPrefix[-1] = self.addPrefix[-1] * m % 1000000007
        self.multPrefix[-1] = self.multPrefix[-1] * m % 1000000007


    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr): 
            return -1
        
        factor = self.multPrefix[-1] * pow(self.multPrefix[idx], 1000000005, 1000000007) #modular inverse
        increment = self.addPrefix[-1] - self.addPrefix[idx] * factor
        
        return (self.arr[idx] * factor + increment) % 1000000007

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
