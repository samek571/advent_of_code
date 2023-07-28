class Solution:
    '''the main fucking point is to use ds that make our look up / store time as efficient as possible
    in this case hashmap comes in mind along with prefix sums
    - prefix sums lets us get any subarray sum in O(1)
    - hashmap is gonna help us (some might know it as a dp equivalent) in keeping the count
    of the subarray sum%k before the element i in iteration'''
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hsh=collections.defaultdict(int)
        hsh[0]=1 # since prefix sum are built upon 0

        actual_prefix=0 ; resultis=0
        for i in nums:
            actual_prefix+=i

            modded = actual_prefix%k

            resultis += hsh[modded]
            hsh[modded]+=1

        return resultis
