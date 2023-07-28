class Solution:
    def specialArray(self, nums) -> int:
        n = len(nums)
        nums.sort()

        for i in range(1, n + 1):
            target = i

            if nums[n - i] >= target:
                if (n - i > 0 and nums[n - 1 - i] < target) or n - i == 0:
                    return target

        return -1

def main():
    sol = Solution()
    print(sol.specialArray([3,5]))

if __name__ == "__main__": main()