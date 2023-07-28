def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    #faster
    # s.reverse()
    # return s


    #recursion
    def helper(left, right, string):
        #exit vetva
        if left >= right:
            print(s)
            return

        s[left], s[right] = s[right], s[left]

        helper(left + 1, right - 1, s)

    helper(left=0, right=len(s) - 1, string=s)



print(reverseString(["a","b","c","d"]))