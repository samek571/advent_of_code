class Solution:
    def num_subarrays_with_k_distinct(self, arr, k):
        num_subarrays = 0
        left = 0
        right = 0
        element_count = {}
        while right < len(arr):
            element_count[arr[right]] = element_count.get(arr[right], 0) + 1
            while len(element_count) > k:
                element_count[arr[left]] -= 1
                if element_count[arr[left]] == 0:
                    del element_count[arr[left]]
                left += 1
            num_subarrays += right - left + 1
            right += 1
        return num_subarrays

    
    
    #exactly k is basically <0, k> without <0, k-1> #same fuckery as 6! = 6*5!
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.num_subarrays_with_k_distinct(nums, k) - self.num_subarrays_with_k_distinct(nums, k-1)
