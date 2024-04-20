class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:

        # it is kinda clear that in order to b be in a, a has to be at least that big
        # therefore we have a starting point from which we are going to try further
        #
        # next thought is how far do we go, its gonna get tle if we physically store very big strings
        # well... if is has the same lenght there might happen it just didnt match by a close inch 
        # (a = "abcd", b = "cdabcdab" --> starting is abcdabcd, both lenghts are 8 but it doesnt match yet)
        # yet if we add another a to its a{0,} we prevent the slight slip up
        # because it might have happened just that its not exactly (abcd, abcdabcd), simply some offset like the first testcase, if it really isnt there return -1


        multiply = math.ceil(len(b)/len(a))
        
        # if b in a*multiply : return multiply
        # elif b in a*(multiply+1): return multiply+1
        # return -1

        # works because if first fails, its bool False which is 0 and 0*n=0
        # OR works by taking 1 if there is at least one in a stram of 0
        # therefore if its not in the first match nor second, its gonna be at least in the last one cuz -1 does exists 
        return multiply * (b in a*multiply) or (1+multiply) * (b in a*(multiply+1)) or -1
