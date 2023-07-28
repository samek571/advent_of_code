import itertools

class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        subsets = set()
        for n in range(len(nums) + 1):
            subsets.update(itertools.combinations(nums, n))
        return list(subsets)


def main():
    sol = Solution()
    print(sol.subsetsWithDup([1,2,2]))
    print(sol.subsetsWithDup([1,2,3]))
    print(sol.subsetsWithDup([1,2,3,4]))
    print(sol.subsetsWithDup([1]))
    print(sol.subsetsWithDup([1,2]))

if __name__ == "__main__": main()