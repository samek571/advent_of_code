class Solution:
    def searchRange(nums, target: int):

        def exact_interval(i,j):
            while i>=0 and nums[i] == target: i-=1
            while j<len(nums) and nums[j] == target: j+=1
            return [i+1, j-1]

        def binary(start, end):
            if not nums: return [-1,-1]

            while start<=end:
                mid = (start+end)//2

                if target == nums[mid]: return exact_interval(mid, mid)
                elif target<nums[mid]: end=mid-1
                else: start = mid+1

            return [-1,-1]

        return binary(0, len(nums)-1)


    print(searchRange([5,7,7,8,8,10], target = 8))
    print(searchRange([], 0))
    print(searchRange([5,7,7,8,8,10], target = 6))