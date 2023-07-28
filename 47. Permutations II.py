from itertools import permutations

class Solution:
    def permuteUnique(self, nums):
        nums = list(set(permutations(nums)))

        for i in range(len(nums)):
            nums[i]=list(nums[i])

        return nums



def main():
    sol = Solution()
    print(sol.permuteUnique([1,3,2]))
    print(sol.permuteUnique([1,1,2]))

if __name__ == "__main__": main()
