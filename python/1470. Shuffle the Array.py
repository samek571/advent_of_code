class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        massive = []


        for i in range(n):
            massive.append(nums[i])
            massive.append(nums[i+n])
        
        return massive
