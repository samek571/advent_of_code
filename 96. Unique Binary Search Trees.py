import math
class Solution:
    def numTrees(n: int) -> int:

        return int((math.factorial(2*n) / (math.factorial(n+1) * math.factorial(n))))
    print(numTrees(6))
    print(numTrees(7))