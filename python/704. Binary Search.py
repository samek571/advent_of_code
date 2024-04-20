class Solution:
    def search(nums, target) -> int:
        if len(nums) == 1:
            if target in nums: return 0
            else: return -1

        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start + end) // 2

            if target == nums[mid]: return mid
            elif target < nums[mid]: end = mid - 1
            else: start = mid + 1

        return -1

    print(search([-1,0,3,5,9,12], target = 9))  #4
    print(search([-1,0,3,5,9,12], target = 2))  #-1
    print(search([1], target = 1))
    print(search([1], target = 0))
    print("prehasdalsd")
    print(search([2], target = 2))
    print(search([1,2], target = 2))
    print(search([1,5], target = 2))
    print(search([-5, 5], target = 2))

