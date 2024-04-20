class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        dp = [0] * 50001
        for i,j,shift in shifts:
            shift = shift if shift != 0 else -1
            dp[i] += shift ; dp[j+1] -= shift
        
        
        val = 0 ; shifted_s = ""
        for i in range(len(s)):
            val = (val + dp[i]) % 26
            shifted_s += chr(ord('a') + (ord(s[i]) - ord('a') + val) % 26)
        return shifted_s
