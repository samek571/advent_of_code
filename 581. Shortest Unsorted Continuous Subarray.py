class Solution:
    def findUnsortedSubarray(self, nums):
        new = sorted(nums)
        if nums == new or len(nums) == 1: return 0

        left, right = 0, 0
        while nums[left] == new[left]: left+=1
        while nums[-right-1] == new[-1-right]: right+=1

        return len(nums)-right-left



def main():
    sol = Solution()
    print(sol.findUnsortedSubarray([2,6,4,8,10,9,15]))
    print(sol.findUnsortedSubarray([2]))
    print(sol.findUnsortedSubarray([2,1]))
    print(sol.findUnsortedSubarray([1,2]))
    print(sol.findUnsortedSubarray([1,2,3,4]))

if __name__ == "__main__": main()