from itertools import defaultdict

class Solution:
    def fourSumCount(nums1, nums2, nums3, nums4) -> int:
        # z nejakeho titulu nahovno
        # setaz=set()
        #
        # for third in nums3:
        #     for fourth in nums4:
        #         setaz.add(-1*(fourth+third))
        #
        # conter=0
        # for first in nums1:
        #     for second in nums2:
        #         if first+second in setaz: conter+=1
        #
        # return conter

        mapa=defaultdict(int)

        for third in nums3:
            for fourth in nums4:
                mapa[-(fourth+third)] +=1

        conter=0
        for first in nums1:
            for second in nums2:
                if first+second in mapa.keys(): conter+=mapa[first+second]

        return conter

    print(fourSumCount([1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]))
    print(fourSumCount([0], nums2 = [0], nums3 = [0], nums4 = [0]))