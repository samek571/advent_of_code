import math
class Solution:
    def isPowerOfTwo(n: int) -> bool:

        if n <= 0: return False

        # elif (n & (n - 1)) == 0: return True
        # else: return False

        return (n & (n - 1)) == 0

    print(isPowerOfTwo(2 ** 6))
    print(isPowerOfTwo(2 ** 0))
    print(isPowerOfTwo(2 ** 1))
    print(isPowerOfTwo(2 ** 2))
    print(isPowerOfTwo(2 ** 4))
    print(isPowerOfTwo(2 ** 8))
    print(isPowerOfTwo(2 ** 10))
    print(isPowerOfTwo(17))
    print(isPowerOfTwo(256))
    print(isPowerOfTwo(2 ** 16))
    print(isPowerOfTwo(0))