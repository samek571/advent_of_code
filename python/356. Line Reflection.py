import collections


class Solution:
    def isReflected(self, points):# List[List[int]]) -> bool:
        points = list({(x,y) for x,y in points})
        sotred = sorted(points, key=lambda x: x[0])
        hsh = collections.defaultdict(list)

        for x,y in sotred:
            hsh[y].append(x)


        line = None
        tmp = hsh[points[0][1]] #list
        if len(tmp) % 2 == 1:
            line = tmp[len(tmp)//2]
        else:
            line = (tmp[0] + tmp[-1] )/2



        for y, xesex in hsh.items():
            n = len(xesex)
            if n%2==1 and xesex[n//2] != line: return False


            for i in range(n//2):
                if line != (xesex[n-1-i]+xesex[i])/2: return False

        return True

def main():
    sol = Solution()
    print(sol.isReflected(points = [[1,1],[-1,1]]))
    print(sol.isReflected(points = [[1,1],[-1,-1]]))
    print(sol.isReflected(points = [[1,1],[-1,1], [2,1], [-2,1]]))
    print(sol.isReflected(points = [[1,1],[-1,1], [2,1], [-2,1], [0,0]]))
    print(sol.isReflected(points = [[1,1],[-1,1], [2,1], [-2,1], [0,0], [-2, 1]]))
    print(sol.isReflected(points = [[1,1]]))
    print(sol.isReflected(points = [[1,1]]))

if __name__ == "__main__": main()



# without duplicated points...
"""

        sotred = sorted(points, key=lambda x: x[0])
        hsh = collections.defaultdict(list)

        for x,y in sotred:
            hsh[y].append(x)


        line = None
        tmp = hsh[points[0][1]] #list
        if len(tmp) % 2 == 1:
            line = tmp[len(tmp)//2]
        else:
            line = (tmp[0] + tmp[-1] )/2



        for y, xesex in hsh.items():
            n = len(xesex)
            if n%2==1 and xesex[n//2] != line: return False


            for i in range(n//2):
                if line != (xesex[n-1-i]+xesex[i])/2: return False

        return True

"""