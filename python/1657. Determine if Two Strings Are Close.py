from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return set(word1) == set(word2) and Counter(Counter(word1).values()) == Counter(Counter(word2).values())

def main():
    sol = Solution()
    print(sol.closeStrings("abss", "serr"))
    print(sol.closeStrings("abss", "saba"))

if __name__ == "__main__": main()