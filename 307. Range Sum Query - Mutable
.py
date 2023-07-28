#segment tree ofc
class NumArray:

    def __init__(self, nums: List[int]):
        if len(nums) > 0:
            self.n = len(nums)
            self.tree = [0] * (2 * self.n)
            self.build_tree(nums)
    
    def build_tree(self, nums):
        for i in range(self.n, 2 * self.n):
            self.tree[i] = nums[i - self.n]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, i: int, val: int) -> None:
        i += self.n
        self.tree[i] = val
        while i > 0:
            left = i
            right = i
            if i % 2 == 0:
                right = i + 1
            else:
                left = i - 1
            self.tree[i // 2] = self.tree[left] + self.tree[right]
            i //= 2

    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        total_sum = 0
        while left <= right:
            if left % 2 == 1:
                total_sum += self.tree[left]
                left += 1
            if right % 2 == 0:
                total_sum += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return total_sum

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
