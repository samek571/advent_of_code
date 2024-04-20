import math


class Solution:
    def binaryGap(n: int) -> int:
        if (n and (not(n & (n - 1))) ): return 0
        n=bin(n)[2:]

        output = 0
        lastpos=0
        current=0
        for i in range(len(n)):
            if n[i] == "1":

                lastpos = current
                current = i
                output = max(output, current-lastpos)

        return output

    print(binaryGap(5))
    print(binaryGap(1))
    print(binaryGap(3))
    print(binaryGap(22))
    print(binaryGap(8))
