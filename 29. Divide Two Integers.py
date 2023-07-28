import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        s = str(eval(str(dividend)+"/"+str(divisor)))
        return min(int(s[:s.index(".")]), 2**31-1)


def main():
    sol = Solution()
    print(sol.divide(10, 3))
    print(sol.divide(4710, 23))
    print(sol.divide(8, -3))
    print(sol.divide(7, -3))
    print(sol.divide(15, 5))
    print(sol.divide(-2147483648, -1))

if __name__ == "__main__": main()