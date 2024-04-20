class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if 2 >= n: return n
        
        max_len = 0 ; window_start = 0 ; char_freq = {}
        for window_end in range(n):
            right_char = s[window_end]
            
            if right_char not in char_freq:
                char_freq[right_char] = 0
            
            char_freq[right_char] += 1
            
            while len(char_freq) > 2:
                left_char = s[window_start]
                char_freq[left_char] -= 1
                if char_freq[left_char] == 0:
                    del char_freq[left_char]
                window_start += 1
            
            
            max_len = max(max_len, window_end - window_start + 1)
        
        
        return max_len
