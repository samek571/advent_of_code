import math

class Solution:
    def numSquares(n: int) -> int:

        # Perfect square straight away O(1)
        # Not sure if it is the fastest way tho :/
        if math.sqrt(n)%1 == 0:
            return 1

        #sum of two squares O(sqrt(n))
        hashmap = dict()
        for i in range(n):
            if i * i > n:
                break

            hashmap[i * i] = 1

            if (n - i * i) in hashmap.keys():
                return 2

       #Legendre's three-square theorem O(log(n))
        while n > 0 and n % 4 == 0:
            n /= 4
        if n % 8 != 7:
            return 3
        else:   #Lagrange's four-square theorem
            return 4

    print(numSquares(13))   #2
    print(numSquares(12))   #3
    print(numSquares(21))   #3
    print(numSquares(15))   #4
    print(numSquares(250))  #2
    print("hovno")
    print(numSquares(14))   #3

'''
5   4+1
6   4+1+1
7   4+1+1+1
8   4+4
9   9
10  9+1
11  9+1+1
12  4+4+4
13  9+4
14  9+4+1
15  9+4+1+1
16  16
17  16+1
18  9+9
19  9+9+1
20  16+4
21  16+4+1
22  9+9+4
23  9+9+4+1
24  16+4+4
25  25
'''