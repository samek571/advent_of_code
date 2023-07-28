# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        flag = False
        num = n/2
        beg = 1
        end = n
        
        
        while flag == False:
            num = beg+ (end-beg)//2
            theVal = guess( num)
            if theVal == -1:
                end = num-1
            elif theVal == 1:
                beg = num+1
            else:
                flag = True
                return num
        return -1
