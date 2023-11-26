class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        bruteforce O(n^2) is pretty simple and concience --> for each pile we keep tracking the minimum from its right and the lenght, updating the glboal max after each expansion
        [3, 1, 5] we have
        3, 2, 3
        1, 2
        5

        for [3, 2, 5, 1] we have
        1*3, 2*2, 3*2, 4*1
        1*2, 2*2, 3*1
        1*5, 2*1
        1*1

        '''

        '''
        idea for improved tactic is pretty clear aswell --> we simulate flood that is rising
        first we have just one flat rectangle with area of lenght*min, after the water rises a bit
        there this smallest element is out of the game leaving us with at least one (but very possible more) subarrays in which we can do the same, measure the lenght in O(1) and next min is already known aswell so there is really going to be just O(n) operation made

        suppose [3,5,2,1,5,6,2,3] and table in this format  flood with min: len*min
        1: 8*1
        2: 3*2, 4*2
        3: 2*3, 2*5, 1*3
        5: 1*5, 2*5
        6: 1*6
        '''

        #or it could be done like this...
        s = []
        max_area = 0
        idx = 0

        while idx < len(heights):
            if not s or heights[s[-1]] <= heights[idx]:
                s.append(idx)
                idx += 1
            else:
                top_of_stack = s.pop()
                area = (heights[top_of_stack] * ((idx - s[-1] - 1) if s else idx))
                max_area = max(max_area, area)

        while s:
            top_of_stack = s.pop()
            area = (heights[top_of_stack] * ((idx - s[-1] - 1) if s else idx))
            max_area = max(max_area, area)

        return max_area
