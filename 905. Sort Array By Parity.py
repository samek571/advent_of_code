class Solution:
    def sortArrayByParity(self, nums):

        return [i for i in nums if i%2==0] + [i for i in nums if i%2==1]


def main():
    sol = Solution()
    print(sol.sortArrayByParity([3,2,1,4]))

if __name__ == "__main__": main()