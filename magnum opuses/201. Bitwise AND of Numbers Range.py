import math

"""https://leetcode.com/problems/bitwise-and-of-numbers-range/solutions/2947281/python-using-math-explained-beats-97"""
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left == right or left == 0: return left

        l,r = math.floor(math.log(left, 2)), math.floor(math.log(right, 2))
        if l!=r: return 0


        ans = left
        for num in range(left + 1, right + 1):
            ans = ans & num
        return ans


def main():
    sol = Solution()
    print(sol.rangeBitwiseAnd(9, 10))
    print(sol.rangeBitwiseAnd(18, 19))
    print(sol.rangeBitwiseAnd(17, 25))
    print(sol.rangeBitwiseAnd(5, 7))
    print(sol.rangeBitwiseAnd(17, 23))
    print(sol.rangeBitwiseAnd(17, 22))
    print(sol.rangeBitwiseAnd(0,0))
    print(sol.rangeBitwiseAnd(1, 214356))
    print(sol.rangeBitwiseAnd(1, 2))

if __name__ == "__main__": main()
