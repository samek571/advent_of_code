from collections import defaultdict

class Solution:
    def leastBricks(wall) -> int:

        gaps=defaultdict(int)
        for layer in wall:
            position=0
            for brick in layer[:-1]:
                position+=brick
                gaps[position]+=1

        crosses=list(gaps.values())
        if not crosses: return len(wall)
        else:
        #print({key: val for key, val in sorted(gaps.items(), key = lambda ele: ele[0])})
            return len(wall) - max(list(gaps.values()))

    print(leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))
    print(leastBricks([[1],[1],[1]]))
    print(leastBricks([[1],[1],[1]]))
