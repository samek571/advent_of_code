class Solution:
    def reverse(x: int) -> int:

        # # handling size part1
        # if (x>2**31-1 and x%10!=0) or (x<-2**31 and x%10!=0):
        #     return 0

        x=str(x)
        # all negatives
        if x[0]=="-":
            x = x[1:]
            x = x[::-1]
            x=-int(x)
            if not x<-2**31:
                return x
            else:
                return 0

        # all positive integers
        else:
            x=x[::-1]
            x=int(x)
            if not x>2**31-1:
                return x
            else:
                return 0


    print(reverse(13400))
    print(reverse(123))
    print(reverse(-123))
    print(reverse(120))
    print(reverse(0))

    print(reverse(-10))
    print(reverse(-10000000000000000))
    print(reverse(123123))