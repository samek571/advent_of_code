from collections import defaultdict

class Solution:
    def numPairsDivisibleBy60(time) -> int:
        map=defaultdict(int)

        for i in time:
            map[i%60]+=1

        totale=0
        full = map[0]
        full = (full*(full-1))//2
        half = map[30]
        half = (half*(half-1))//2
        totale+= half+full

        del map[0]
        del map[30]
        print(map)

        for i in range(1, 30):
            totale+=map[60-i]*map[i]

        return totale


    print(numPairsDivisibleBy60([30,20,150,100,40]))
    print(numPairsDivisibleBy60([60,60,60,60]))
    print(numPairsDivisibleBy60([60,60,60,60,60]))
    print(numPairsDivisibleBy60([30,30,30,30,30]))
    print(numPairsDivisibleBy60([50,50,50,50,50,10,10,10,10]))