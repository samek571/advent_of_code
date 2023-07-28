from collections import defaultdict

class Solution:
    def originalDigits(self, s: str) -> str:
        freq_map = defaultdict(int)
        for c in s:
            freq_map[c] += 1

        ans = ''
        digit_map = {'z': ('0', "zero"), 'w': ('2', "two"), 'u': ('4', "four"), 'x': ('6', "six"),
                     'g': ('8', "eight"), 'o': ('1', "one"), 't': ('3', "three"), 'f': ('5', "five"),
                     's': ('7', "seven"), 'i': ('9', "nine")}
        for char, (digit, word) in digit_map.items():
            digit_freq = freq_map[char]
            for i in range(digit_freq):
                ans += digit
            for c in word:
                freq_map[c] -= digit_freq

        return ''.join(sorted(ans))
