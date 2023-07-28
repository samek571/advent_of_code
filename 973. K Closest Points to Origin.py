import math
from collections import defaultdict

#could be done with a binary search

class Solution:
    def kClosest(points, k):

        dick=defaultdict(int)

        for i in range(len(points)):
            distance = math.sqrt(points[i][0]**2 + points[i][-1]**2)
            # if not i in dick:
            dick[i] = distance

        sortedpenis = dict(sorted(dick.items(), key=lambda x: x[1]))
        # print(sortedpenis)
        #
        # output=[]
        # while True:
        #     for key, val in sortedpenis.items():
        #         output.append(points[key])
        #         k-=1
        #         if k==0: return output




    print(kClosest([[1,3],[-2,2]], k = 1))
    print(kClosest([[1,3],[-2,2], [8,9]], k = 2))