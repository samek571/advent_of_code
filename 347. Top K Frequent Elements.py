from heapq import nlargest
class Solution:
    def topKFrequent(nums, k: int):
        ht=dict()

        #adding in ht
        for i in range(len(nums)):
            if nums[i] in ht:

                ht[nums[i]]+=1
            else:
                ht[nums[i]]=1

        return nlargest(k, ht, key=ht.get)


    print(topKFrequent([1,1,2,2,2,3], 2))
    print(topKFrequent([1], 1))