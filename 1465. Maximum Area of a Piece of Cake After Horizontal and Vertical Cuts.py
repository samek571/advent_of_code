class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts) -> int:
        horizontalCuts += [h, 0]
        verticalCuts += [w, 0]

        horizontalCuts.sort()
        verticalCuts.sort()
        prev_hor, prev_ver, hmax,vmax = 0,0, 1,1

        for num in horizontalCuts:
            hmax = max(num-prev_hor, hmax)
            prev_hor = num

        for num in verticalCuts:
            vmax = max(num-prev_ver, vmax)
            prev_ver = num

        return (vmax*hmax) %(10**9+7)

def main():
    sol = Solution()
    print(sol.maxArea(h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]))
    print(sol.maxArea(h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]))
    print(sol.maxArea(h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]))
    print(sol.maxArea(h = 1000000000, w = 1000000000, horizontalCuts = [2], verticalCuts = [2]))

if __name__ == "__main__": main()