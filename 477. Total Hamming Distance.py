class Solution:
    def totalHammingDistance(nums) -> int:
        bits=[0]*32

        for num in nums:
            i = 0
            while num:
                bits[i] += num & 1
                num >>= 1
                i += 1

        total = 0
        for num in nums:

            for i in range(32):
                if not num & 1:
                    total += bits[i]
                num = num >> 1


        return total

    print(totalHammingDistance([4,14,2]))