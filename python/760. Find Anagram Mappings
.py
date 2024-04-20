class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        hsh = collections.defaultdict(list)

        for i, num in enumerate(nums2):
            hsh[num].append(i)

        o = []
        for i, num in enumerate(nums1):
            o.append(hsh[num].pop())
        
        return o
