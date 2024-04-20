# The knows API is already defined for you.
# return a bool, whether a knows b
def knows(a: int, b: int) -> bool:

# who knows the first dude
# everyone who he knows; test iteratively if is known by everyone else in the game
# done.
class Solution:
    '''
    its clear that if he knows someone its bad, as well as if not everyone knows him.

    we are playing statistic here and probably leetcode thought of this approach,
    so picking 0 regardless can make it fully connected mesh in the worst scenario of n^2
    I could optimize it ofc just there is no purpose to compete in little details especially if
    it has 0 contributed value
    '''
    def findCelebrity(self, n: int) -> int:
        dude = 0
        for i in range(1, n):
            if knows(dude, i): dude = i
            # we can do it since till now the "suspected celebrity" knew someone
            # therefore noone from them [0, i) can be an adept

        for i in range(n):
            if i != dude:
                if not knows(i, dude) or knows(dude, i):
                    return -1

        return dude


