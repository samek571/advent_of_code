import collections
class Solution:
    '''
    two pointers, dictionary } sliding window algorithm
    '''

    def minWindow(s: str, t: str) -> str:
        #nonsense case
        if len(s)<len(t): return ""

        need, missing = collections.Counter(t), len(t)
        i = left = right = 0
        for j, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

            # if we have at least some window ->
            # starting to shorten the window
            if not missing:

                # while we dont find some element from t ->
                # moving left pointer
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1

                # comparing shortest window with actual
                if not right or j - i <= right - left:
                    left, right = i, j
        return s[left:right]


    print(minWindow("sjdwbfuhsbs__so", "sos"))
    print(minWindow("psaciehovanko", "oa"))
    print(minWindow("ahorao", "oa"))
    print(minWindow("ahoraoss", "s"))
    print(minWindow("as", t = "aa"))
    print(minWindow("af", t = "ad"))
    print(minWindow("ADOBECODEBANC", t = "ABC"))

