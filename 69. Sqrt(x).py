class Solution:
    def mySqrt(x):
        # for i in range(2**31):
        #     if i**2>x: return i-1

        left = 0
        right = x
        while (left<=right):
            middle=(left+right)//2

            if middle**2 <= x and x < (middle+1)**2: return middle
            elif middle**2 > x: right = middle-1
            else: left = middle+1

    print(mySqrt(10))
    print(mySqrt(1000))
    print(mySqrt(0))
    print(mySqrt(8))
    print(mySqrt(4))
