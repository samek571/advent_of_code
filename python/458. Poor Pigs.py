import math
class Solution:
    def poorPigs(buckets: int, minutesToDie, minutesToTest: int) -> int:
        # shots=(minutesToTest//minutesToDie)+1
        # return math.ceil((math.log(buckets ,shots)))

        #one liner
        #return math.ceil((math.log(buckets ,(minutesToTest//minutesToDie)+1)))

        #faster one liner
        return (math.ceil(math.log(buckets) / math.log(minutesToTest // minutesToDie + 1)))

    print(poorPigs(4, minutesToDie = 15, minutesToTest = 30))
    print(poorPigs(4, minutesToDie = 15, minutesToTest = 15))
    print(poorPigs(1000, minutesToDie = 15, minutesToTest = 60))