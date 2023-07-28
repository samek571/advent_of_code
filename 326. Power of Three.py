import math

class Solution:
    def isPowerOfThree(n: int) -> bool:
        if n <= 0: return False

        return (math.log10(n) / math.log10(3)) == math.floor((math.log10(n) / math.log10(3)))

    print(isPowerOfThree(243))
    print("\n")
    print(isPowerOfThree(27))
    print(isPowerOfThree(0))
    print(isPowerOfThree(9))
    print(isPowerOfThree(45))
