class Solution:
    def maxDistance(self, nums1, nums2) -> int:
        distance = 0

        for i in range(len(nums1)):
            start = i
            end = len(nums2)-1
            while start<= end:
                mid = (start+end)//2

                if nums2[mid] < nums1[i]:
                    end = mid-1
                else:
                    start = mid+1
            distance = max(distance, end -i)

        return distance