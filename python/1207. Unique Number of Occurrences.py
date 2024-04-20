class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        stt, dck = set(), defaultdict(int)

        for i in arr:
            dck[i] += 1

        for v in dck.values():
            if v in stt: return False
            else: stt.add(v)

        return True
