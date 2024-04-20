class Solution:
    def minSteps(self, s: str, t: str) -> int:
        return len(s) - sum((collections.Counter(s) & collections.Counter(t)).values())
