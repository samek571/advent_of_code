import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        hsh = collections.Counter(s)

        is_one= False
        at_least_two = 0
        for val in hsh.values():
            at_least_two += val//2

            if val%2 == 1: is_one = True

        if is_one: at_least_two = 2 * at_least_two +1
        else: return 2* at_least_two



