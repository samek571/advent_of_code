class Solution:
    # O(n) plain manachers algo
    def longestPalindrome(self, s) -> str:

        # Preprocess the string
        processed_string = "#".join("^{}$".format(s))
        n = len(processed_string)
        P = [0] * n
        C = R = 0

        for i in range(1, n - 1):
            if R > i:
                mirror = 2 * C - i
                P[i] = min(R - i, P[mirror])

            while processed_string[i + 1 + P[i]] == processed_string[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > R:
                C = i
                R = i + P[i]

        # Find the maximum palindrome length and center position
        max_length = max(P)
        center_index = P.index(max_length)

        # Extract the palindrome substring from the original string
        start = (center_index - 1 - max_length) // 2
        end = start + max_length

        return s[start:end]
