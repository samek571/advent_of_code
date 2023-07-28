import math
class Solution:
    def minOperations(n: int) -> int:
        if n%2==0:
            return int((n/2)**2)
        else:
            hovno=math.floor(n/2)
            return hovno*(hovno+1)

    print(minOperations(7))
    print(minOperations(8))

'''
2->1
4->2
6->9
8->16
10->25
12->36

1->0
3->2
5->6
7->12
9->20
'''