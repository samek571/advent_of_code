class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        if n * k < target: return 0

        answer = 0
        for p in range((target-1) // k + 1):  # binominal distribution - ugly but nice math
            answer += (-1) ** p * math.comb(n, p) * math.comb(target - p*k - 1, n - 1)
            answer %= 10 ** 9 + 7
        
        return answer
