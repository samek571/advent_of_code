class Solution:
    def minSubArrayLen(self, target: int, nums):# List[int]) -> int:
        o, i, j, summage = float('inf'), 0, 0, 0

        while j < len(nums):
            summage+=nums[j]
            j+=1

            while summage >= target:
                o = min(o, j-i)
                summage-=nums[i]
                i+=1

        if o == float('inf'): return 0
        return o


def main():
    sol = Solution()
    print(sol.minSubArrayLen(15, nums = [1,2,3,4,5]))
    print(sol.minSubArrayLen(7, nums = [1,1,1,1,7,1]))
    print(sol.minSubArrayLen(7, nums = [1,1,1,1,7]))
    print(sol.minSubArrayLen(7, [2,3,1,2,4,3]))
    print(sol.minSubArrayLen(4, nums = [1,4,4]))
    print(sol.minSubArrayLen(11, nums = [1,1,1,1,1]))

if __name__ == "__main__": main()

# o = float('inf')
#
# for i in range(len(nums)):
#     tmp_sum = nums[i]
#     j = i + 1
#     while j < len(nums) and tmp_sum < target:
#         tmp_sum += nums[j]
#         j += 1
#
#     if tmp_sum >= target:
#         o = min(j - i, o)
#
# if o == float('inf'): return 0
# return o