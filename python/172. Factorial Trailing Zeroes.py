class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt = 0

        i=1
        while 10**4>5**i:
            cnt+=n//(5**i)
            i+=1

        return cnt


def main():
    sol = Solution()
    print(sol.trailingZeroes(0))
    print(sol.trailingZeroes(7))
    print(sol.trailingZeroes(11))
    print(sol.trailingZeroes(26))

if __name__ == "__main__": main()
