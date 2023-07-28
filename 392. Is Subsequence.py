class Solution:
    def isSubsequence(s: str, t: str) -> bool:
        l = len(s)
        place = 0
        for x in t:
            if place < l and x == s[place]:
                place += 1
        return l <= place