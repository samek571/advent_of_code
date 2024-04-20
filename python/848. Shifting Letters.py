from datetime import datetime

class Solution(object):
    def shiftingLetters(s, shifts):
        """
        :type s: str
        :type shifts: List[int]
        :rtype: str
        """
        start_time = datetime.now()
        #o(n)
        sumaz=sum(shifts)
        output=''
        alfabeta="abcdefghijklmnopqrstuvwxyz"

        for i in range(len(s)):
            alphabeta_index = alfabeta.index(s[i])

            output= output + alfabeta[(alphabeta_index+sumaz)%26]
            sumaz= sumaz-shifts[i]

        end_time = datetime.now()
        print(('Duration: {}'.format(end_time - start_time)))
        return output
    print(shiftingLetters("aaa", [1,2,3]))
    print(shiftingLetters("abc", [3, 5, 9]))
