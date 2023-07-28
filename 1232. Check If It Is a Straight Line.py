class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0,y0), (x1, y1)= coordinates[:2]
        return all( (y1-y0) * (x-x1) == (x1-x0) * (y-y1) for x,y in coordinates)
