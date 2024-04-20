import math
class Solution:
    def isPowerOfFour(n: int) -> bool:
        if n<=0: return False

        elif (math.sqrt(n))**2==n and (n & (n-1))==0: return True
        else: return False



    print(isPowerOfFour(2**6))
    print(isPowerOfFour(2**0))
    print(isPowerOfFour(2**1))
    print(isPowerOfFour(2**2))
    print(isPowerOfFour(2**4))
    print(isPowerOfFour(2 ** 8))
    print(isPowerOfFour(2 ** 10))
    print(isPowerOfFour(17))
    print(isPowerOfFour(256))
    print(isPowerOfFour(2**16))
    print(isPowerOfFour(0))