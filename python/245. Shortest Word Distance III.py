class Solution:
    def shortestWordDistance(self, wordsDict, word1: str, word2: str) -> int:
        first, second, o = -1, -1, len(wordsDict)

        for i, w in enumerate(wordsDict):
            if w == word1:
                first=i
                if second != -1: o = min(o, abs(second-first))

            if word2 == w:
                second=i
                if first != -1 and first != second: o = min(o, abs(second-first))

        return o


def main():
    sol = Solution()
    print(sol.shortestWordDistance(wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"    ))
    print(sol.shortestWordDistance(wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"))

if __name__ == "__main__": main()
