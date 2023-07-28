class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp_arr = [0] * (n + 1)
        dp_arr[0], dp_arr[1] = 1, 1

        '''
        LOGIC : For every index, check if the digit alone can be a valid letter, then add 1 to the count of strings that can be formed. 
        Also check if the combination of the current digit and the last digit and see if they form a valid alphabet. If yes, that combination forms another possible string.
        
        E.g. : 11106 -> (1, 1106) + (11, 106) ---> 2 strings possible till now
                            |           |
                        (A, 1106)    (K, 106)
                        
                        ..... and so on for the whole string.
        '''

        # If the first character is zero, then no valid string is possible
        if s[0] == "0":
            return 0
        else:
            for i in range(2, n + 1):
                if 1 <= int(s[i - 1]) <= 9:
                    dp_arr[i] += dp_arr[i - 1]
                if 10 <= int(s[i - 2] + s[i - 1]) <= 26:
                    dp_arr[i] += dp_arr[i - 2]
            return dp_arr[-1]