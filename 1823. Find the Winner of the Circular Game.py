'''
4
4
5
4
6
4
7
4
8
4
9
4
10
4
11
4
12
4
13
4
14
4
15
4
16
4
17
4
18
4
19
4
'''
import math

class Solution:
    def findTheWinner(n: int, k: int) -> int:
        # a = math.floor(math.log(n,k))
        # l = n-k**a
        #
        # if l<k*a: return k*l+1

        buzeranti = list(range(1, n + 1))
        while len(buzeranti) > 1:
            i = (k - 1) % len(buzeranti)
            buzeranti.pop(i)
            buzeranti = buzeranti[i:] + buzeranti[:i]  #to kill kth in line, moving first k-1 is necesearry

        return buzeranti[0]
    print(findTheWinner(19, 4))
    print(findTheWinner(18, 4))
    print(findTheWinner(17, 4))
    print(findTheWinner(4, 4))
    print(findTheWinner(5, 4))
    print(findTheWinner(6, 4))
    print(findTheWinner(7, 4))
    print(findTheWinner(8, 4))
    print(findTheWinner(9, 4))