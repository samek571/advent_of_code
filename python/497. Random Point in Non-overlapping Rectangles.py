import bisect
import random
from itertools import accumulate

class Solution:

    def __init__(self, rects):
        area = [(x2-x1+1)*(y2-y1+1) for x1,y1,x2,y2 in rects]
        self.weights = [i/sum(area) for i in accumulate(area)]
        self.rects = rects

    def pick(self):
        rectangel_idx = bisect.bisect_left(self.weights, random.random())
        x1, y1, x2, y2 = self.rects[rectangel_idx]
        return [random.randint(x1, x2), random.randint(y1, y2)]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
