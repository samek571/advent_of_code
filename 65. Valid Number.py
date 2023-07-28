import  re

class Solution:
    def isNumber(self, s: str) -> bool:
        '''
        ^[+-]? says we are expecting either + or - or nothing at the beginning(^) of the string, nothing because the ? which makes it optional

        inside this first group (?:\d+\.?\d*|\d*\.?\d+) we can see multiple ideas:
            the pipe (|) is simply just OR logical operation --> either stuff before or after the pipe gets executed
            1. * after certain characters makes them repeat any number of times <0, infinity>
            2. \ is really just saying that we dont mean literal letter "d" but the function it represents in regex episode
            3. in this case its \d which is one single digit
            4. adding the + afterwards makes it a continous sequence of digits --> its gonna match a subsequence of digits
            5. doing \. is just saying we mean literal dot and not the purpose of dot "match any characters till the line break"

        second group is easier and pretty much intuitive as if now; ([eE][+-]?\d+)?$
            1. $ at the end there is gonna be something like this, similar to the ^ we have encountered already
            2. [eE] either lowercase or upper operation
            3. [+-]? followed by optional sign
            4. \d+ ending with at least one digit (since we cant have just the letter "e")
            5. )? makes it all optional --> no letter e has to be encountered

        now if we have matched the whole string s we return True, otherwise its not a valid expression
        '''


        x = re.match("^[+-]?(?\d+\.?\d*|\d*\.?\d+)([eE][+-]?\d+)?$"  ,s)
        return x
        #return True if x else False


def main():
    sol = Solution()
    print(sol.isNumber("+4e-4"))
    print(sol.isNumber("+4e"))
    print(sol.isNumber("+4e-"))
    print(sol.isNumber('+-3'))
    print(sol.isNumber('-4.66e-3'))
    print(sol.isNumber('-.66e-3'))
    print(sol.isNumber('-.e-3'))
    print(sol.isNumber('-4.e-3'))
    print(sol.isNumber('0'))
    print(sol.isNumber('0.'))
    print(sol.isNumber('0.e+6'))

if __name__ == "__main__": main()