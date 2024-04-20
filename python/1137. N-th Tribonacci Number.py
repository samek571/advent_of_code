class Solution:
    def tribonacci(n: int) -> int:

        if n==0:
            return 0
        elif n==1 or n==2:
            return 1

        a=0
        b=c=1

        for i in range(n-2):
            d=a+b+c
            a,b,c=b,c,d

        return d


    print(tribonacci(25))