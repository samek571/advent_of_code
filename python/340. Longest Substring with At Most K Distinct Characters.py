class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        ans = 0
        left = 0
        k_char = {}
        for i in range(len(s)):
            if s[i] in k_char:
                k_char[s[i]] += 1
            elif len(k_char) < k:
                k_char[s[i]] = 1
            else:
                ans = max(ans, sum(k_char.values()))
                while len(k_char) == k:
                    k_char[s[left]] -= 1
                    if not k_char[s[left]]:
                        del k_char[s[left]]
                    left += 1
                k_char[s[i]] = 1
                
        ans = max(ans, max(ans, sum(k_char.values())))
        return ans
