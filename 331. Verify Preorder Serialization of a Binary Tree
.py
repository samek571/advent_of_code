class Solution:
    def isValidSerialization(self, preorder: str) -> bool:

        available = 1
        for e in preorder.split(","):
            available-=1
            if available < 0: return False

            if e != "#": available+=2

        return not available
