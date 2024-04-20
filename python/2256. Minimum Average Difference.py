class Solution:
    def minimumAverageDifference(self, nums) -> int:
        summage, n = sum(nums), len(nums)

        left, curr, output = 0, float('inf'), -1
        for i in range(n):
            left+=nums[i]

            if (n - 1 - i)!=0:
                ddd = abs(left // (i + 1) - (summage - left) // (n - 1 - i))
            else:
                ddd = abs(left // (i + 1) - (summage - left))

            if ddd < curr:
                curr = ddd
                output = i

        return output



def main():
    sol = Solution()
    print(sol.minimumAverageDifference(nums = [2,5,3,9,5,3]))
    print(sol.minimumAverageDifference([0]))
    print(sol.minimumAverageDifference([0,0]))
    print(sol.minimumAverageDifference([4,2,0]))

if __name__ == "__main__": main()