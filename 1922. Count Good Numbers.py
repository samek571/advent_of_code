class Solution:
    def countGoodNumbers(n: int) -> int:

        modulaz = 10**9 +7
        odpovet = pow(20, n//2, modulaz)
        if n%2==1: return (5*odpovet)%modulaz
        else: return odpovet%modulaz


    print(countGoodNumbers(4))
    print(countGoodNumbers(5))
    print(countGoodNumbers(6))
    print(countGoodNumbers(7))

'''
1
4
50
345345
2292929
459345903
234234556
123456789097
2
3
4
5
6
7
8
9
10
'''