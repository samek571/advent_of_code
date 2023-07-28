import re
class Solution:
    def isPalindrome(s: str) -> bool:
        # s = ''.join(letter for letter in s if letter.isalnum()).lower()
        # return s==s[::-1]

        #result = re.sub(pattern, repl, string)
        s = re.sub("[^a-zA-Z0-9]+", "", s).lower()
        return s == s[::-1]

    print(isPalindrome("A man, a plan, a canal: Panama"))