class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # indices = [i for i, x in enumerate(flowerbed) if x == 1]

        # x = []
        # for i in range(1, len(indices)):
        #     tmp = indices[i]-indices[i-1]-1
        #     if tmp >= 3:
        #         x.append(tmp//2)

        # return sum( x ) >= n

        count = 1
        beds = 0
        for bed in flowerbed:
            if bed:
                count = 0
            else:
                count += 1
                if count == 3:
                    beds += 1
                    count = 1
        
        if not flowerbed[-1]: 
            count += 1
            if count == 3: beds += 1

        return beds >= n
