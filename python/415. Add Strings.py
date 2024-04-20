class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # one way to do it is via binary numbers
        
        #second looks like this:
        return str(eval(num1 + "+" + num2))

        # and the way it was intended i would perform addition as the first graders do
        # i.e iterate from the end and probably make hashmap in another program which returns 
        # result of 2 strings --> 100 possibilities so it has to be coded

        # or make it via ascii 
