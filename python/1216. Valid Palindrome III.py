from functools import lru_cache

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # check from outside, if there are same elems
        # find the longest palidromic subsequence
        # if len(s) - len(longest) <= k => True
        
        # DP to find the len longest palindromic subsequence
        @lru_cache(maxsize = None)
        def rec(l, r):
            if l == r:
                return 1
            elif l > r or l >= len(s) or r < 0:
                return 0
            
            case1 = rec(l+1, r)
            case2 = rec(l, r-1)
            case3 = 2 + rec(l+1, r-1) if s[l] == s[r] else 0
            return max(case1, case2, case3)
        return len(s) - rec(0, len(s)-1) <= k
