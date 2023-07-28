class Solution:
    def nextGreaterElement(nums1, nums2):
        output = [-1] * len(nums1)
        for i in range(len(nums1)):
            for j in range(nums2.index(nums1[i]), len(nums2)):
                if nums2[j] > nums1[i]:
                    output[i] = nums2[j]
                    break
        return output

    print(nextGreaterElement([4,1,2], nums2 = [1,3,4,2]))