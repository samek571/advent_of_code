class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)

        return sum((n-i)*(i+1) for i, val in enumerate(word) if val in "aeiou")


def main():
    sol = Solution()
    print(sol.countVowels('aba'))
    print(sol.countVowels('abc'))
    print(sol.countVowels('nggr'))

if __name__ == "__main__": main()
