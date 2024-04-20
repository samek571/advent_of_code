class Solution:
    def checkIfPangram(self, s: str) -> bool:
        h=set()

        for i in s:
            if i not in h:
                h.add(i)

        return len(h) == 26
