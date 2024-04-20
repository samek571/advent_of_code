class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # i think it should be labeled as easy or people are genuily fucking stupid
        return re.fullmatch(p, s)
