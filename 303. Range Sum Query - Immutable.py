class NumArray:

    def __init__(self, nums):# List[int]):
        self.nums = nums


        for i in range(1, len(nums)):
            nums[i] = nums[i-1]+nums[i]

        self.nums = [0]+self.nums

    def sumRange(self, left: int, right: int) -> int:
        #if left==0: return self.nums[right]
        return self.nums[right+1]-self.nums[left]



# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(0,2)
print(obj.sumRange(0, 2))
print(obj.sumRange(0, 5))