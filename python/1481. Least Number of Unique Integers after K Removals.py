
#had it in under 15seconds...
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        dick = sorted(Counter(arr).values())
        for i, cnt in enumerate(dick):
            k -= cnt
            if k < 0:
                return len(dick) - i

        return 0
