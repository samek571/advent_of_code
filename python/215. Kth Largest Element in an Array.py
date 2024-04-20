class Solution:
    def findKthLargest(nums,k: int) -> int:
        nums.sort(reverse=True)

        return nums[k-1]

    print(findKthLargest([3,2,1,5,6,4], k = 2))
    print(findKthLargest([3,2,3,1,2,4,5,5,6], k = 4))
    print(findKthLargest([1],1))