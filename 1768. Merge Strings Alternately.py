class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s, l1, l2 = '', len(word1), len(word2)
        mini, maxi = min(l1,l2), max(l1, l2)

        for i in range(mini):
            s+=word1[i]
            s+=word2[i]


        if l1>l2:
            s+=word1[mini:]
        else:
            s+=word2[mini:]

        return s
