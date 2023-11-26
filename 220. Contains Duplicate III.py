from sortedcontainers import SortedList
#nicer than heapq

#also the solution should be in O(n) with some sliding window and bucket sort but who has got the energy ...
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        sorted_list = SortedList()
        for i in range(len(nums)):
            if sorted_list:
                idx = sorted_list.bisect_left(nums[i])
                if idx != len(sorted_list) and sorted_list[idx] - nums[i] <= t:
                    return True

            if sorted_list:
                idx = sorted_list.bisect_left(nums[i])
                if idx != 0 and nums[i] - sorted_list[idx - 1] <= t:
                    return True

            sorted_list.add(nums[i])
            if len(sorted_list) > k:
                sorted_list.remove(nums[i - k])

        return False
