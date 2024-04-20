class Solution:
    def nextPermutation(self, nums) -> None:
        """
        iter backwards and find first nopn increasing element
        if we happen to iterate the whole array (i. e pointer at 0 --> we just [::-1])
        otherwise we dont just copy subarray pre pointer and find particular element that is just
        little bit bigger than our sequence breaker, fix that and reverse the rest of the array
        """

        i = j = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i == 0:
            nums[:] = nums[::-1] #; return
            return nums

        while nums[j] <= nums[i - 1]:
            j -= 1

        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        nums[i:] = nums[len(nums) - 1:i - 1:-1]

        return nums

def main():
    sol = Solution()
    print(sol.nextPermutation([1,2,3]))
    print(sol.nextPermutation([3,2,1]))
    print(sol.nextPermutation([1,1,5]))

if __name__ == "__main__": main()