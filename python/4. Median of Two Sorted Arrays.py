from itertools import chain

class Solution:
    def findMedianSortedArrays(nums1, nums2) -> float:
        nums1=sorted(chain(nums2,nums1))
        print(nums1)

        #even
        if len(nums1)%2==0: return (nums1[len(nums1)//2-1]+nums1[len(nums1)//2])/2
        #odd
        else: return nums1[len(nums1)//2]

    print(findMedianSortedArrays([1,23,4,5], [1,9,9,4]))    #4.5
    print(findMedianSortedArrays([1,3],[2,4]))              #2.5
    print(findMedianSortedArrays([1,2,3],[5,9]))            #3
    print(findMedianSortedArrays([2,1],[]))
    #print(findMedianSortedArrays([],[]))       #constrains dont allow us
