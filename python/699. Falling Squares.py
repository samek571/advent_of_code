from sortedcontainers import SortedList

class Solution:
    '''each sq has starting left drop pos. Right is left+height-1 because
    we can put 2 boxes at one x pos therefore only starting one matters for each sq '''
    '''problem is just little bit hidden interval parsing:

    - we insert <s, e) or <s, e-1> and we have 3 ways to go. 
        One is to be place in the middle of the current boxes
        on top of left One
        on top of right One
    every other notations in the new sq interval has to be removed and 2 new ends are marked.

    achieving this by sorted list is more of a syntax konwledge, boring and not interesting

    '''

    def fallingSquares(self, positions):
        sl = SortedList()
        ans = []
        tallest = 0

        for left, length in positions:
            idx = sl.bisect_left((left, 0, 0))
            max_height = 0
            if idx > 0:
                # l_side: left side, l: length, h: height
                l_side, l, h = sl[idx - 1]
                # left side of new square is within range
                if l_side + l > left:
                    max_height = h
                    del sl[idx - 1]
                    sl.add((l_side, left - l_side, h))
                    # new square is in middle of range
                    if l_side + l > left + length:
                        sl.add((left + length, l_side + l - (left + length), h))

            right = left + length
            # while right side of new square is to the right of left side of range
            # (should only run n times total since ranges are being compressed on each iteration)
            while idx < len(sl) and sl[idx][0] < right:
                l_side, l, h = sl[idx]
                max_height = max(max_height, h)
                # new square completely covers range
                if l_side + l <= right:
                    sl.pop(idx)
                # new square covers left side of range
                else:
                    del sl[idx]
                    sl.add((right, l_side + l - right, h))

            tallest = max(max_height + length, tallest)
            sl.add((left, length, max_height + length))
            ans.append(tallest)


        return ans