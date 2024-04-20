class Solution:
    def countVowelStrings(self, n: int) -> int:
        return int((n+1)*(n+2)*(n+3)*(n+4)/24)


def main():
    sol = Solution()
    print(sol.countVowelStrings(33))
    print(sol.countVowelStrings(1))
    print(sol.countVowelStrings(2))
    print(sol.countVowelStrings(3))
    print(sol.countVowelStrings(4))

if __name__ == "__main__": main()