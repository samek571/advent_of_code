class WordDistance:

    def __init__(self, wordsDict: list[str]):
        self.wordsDict = wordsDict

    def shortest(self, word1: str, word2: str) -> int:
        first, second, o = -1, -1, len(self.wordsDict)

        for i, w in enumerate(self.wordsDict):
            if w == word1:
                first = i
                if second != -1: o = min(o, abs(second - first))

            if word2 == w:
                second = i
                if first != -1 and first != second: o = min(o, abs(second - first))

        return o


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)