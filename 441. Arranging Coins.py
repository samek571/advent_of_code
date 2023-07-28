import math
class Solution:
    def arrangeCoins(n: int) -> int:
        return math.floor(((-1+(math.sqrt(1+n*8)))/2))

    print(arrangeCoins(8))
    print(arrangeCoins(2))
    print(arrangeCoins(29))
    print(arrangeCoins(15))
