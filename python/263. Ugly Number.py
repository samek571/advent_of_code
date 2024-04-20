class Solution:
    def isUgly(n: int) -> bool:
        # if n<1:
        #     return False
        #
        # while n!=1:
        #     if n%2==0:
        #         n/=2
        #         continue
        #     elif n%3==0:
        #         n/=3
        #         continue
        #     elif n%5==0:
        #         n/=5
        #         continue
        #     else:
        #         return False
        #
        # return True

    #cudzi kod
        if n == 0:
            return False
        if n == 1:
            return True

        while n % 2 == 0:
            n >>= 1
        while n % 3 == 0:
            n /= 3
        while n % 5 == 0:
            n /= 5

        return n == 1

    print(isUgly(3*5*5*2*2*2*2*5))
    print(isUgly(1))
    print(isUgly(-4))
    print(isUgly(0))
    print(isUgly(12))
    print(isUgly(6))
    print(isUgly(8))
    print(isUgly(14))
    print(isUgly(1))
