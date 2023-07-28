class Solution:
    def isRectangleCover(self, rectangles) -> bool:

        a,b,c,d, area, corners = float("inf"), float("inf"), -1*float("inf"), -1*float("inf"), 0, set()
        for x1,y1,x2,y2 in rectangles:

            #making clear where the downleft and upright corner is
            if x1<=a and y1<=b: a,b = x1,y1
            if x2>=c and y2>=d: c,d = x2,y2


            #area fits
            area += (x2 - x1) * (y2 - y1)
            corners ^= {(x1, y1), (x2, y2), (x1, y2), (x2, y1)}
        return (corners == {(a, b), (c, d), (a, d), (c, b)}) and (area == (d-b)*(c-a))


def main():
    sol = Solution()
    print(sol.isRectangleCover([[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]))
    print(sol.isRectangleCover([[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]))
    print(sol.isRectangleCover([[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]))

if __name__ == "__main__": main()