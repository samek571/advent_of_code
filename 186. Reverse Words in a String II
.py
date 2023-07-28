class Solution:
    '''
    iterating from back to start; while getting nonspace chars keep going
    then 
    1. take the s[p1:p2] in whcih p1:p2 characterizes a word, meaning p1-1 | p2+1 is space or out of bound 
    2. from p1 to p2 by iteration keep appending at the end of the s
    3. make p2-p1+1+1 pops (second +1 because one is empty char in list) starting at p1

    finished
    '''
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        def switch(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        # s = s[::-1]
        switch(0, len(s)-1)

        i, start, end = 0, 0, 0
        while i <= len(s):
            if i == len(s) or s[i] == ' ':
                end = i - 1
                switch(start, end)
                start = i + 1
                end = i + 1 
            i += 1
