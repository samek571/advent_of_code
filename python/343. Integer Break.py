'''
2 - 1 (1*1)
3 - 2 (2*1)
4 - 4 (2*2)
5 - 6 (2*3)
6 - 9 (3*3)
7 - 12 (2*2*3)
8 - 18 (2*3*3)
####
9 - 27 (3*3*3)
10 - 36 (3*3*2*2)
11 - 54 (3*3*3*2)
12 - 81 (3*3*3*3)
####
13 - 108 (3*3*3*2*2)
14 -
'''

class Solution:
    def integerBreak(n) -> int:
        if n == 2:
            return 1
        elif n == 3:
            return 2

        else:
            zvysok = n%3

            if zvysok == 0:
                return int(3**(n/3))
            if zvysok == 1:
                return int(3**(n//3)/3*2*2)
            if zvysok == 2:
                return int (3**(n//3)*2)

    print(integerBreak(15))