class Solution:

    def __init__(self, w: List[int]):
        self.stck = [w[0]]
        
        for val in w[1:]:
            self.stck.append(val+self.stck[-1])

    def pickIndex(self) -> int:
        num = random.randint(1, self.stck[-1])
        return bisect.bisect_left(self.stck, num)


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
