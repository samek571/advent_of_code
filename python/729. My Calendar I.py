from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        self.matrix = SortedList()

    def book(self, start: int, end: int) -> bool:
        idx = self.matrix.bisect_right((start,end))

        if (idx > 0 and self.matrix[idx-1][-1] > start) or \
            (idx < len(self.matrix) and self.matrix[idx][0] < end): return False

        self.matrix.add((start, end))
        return True


        # if self.matrix[-1][-1] > start: return False
        # else: self.matrix.append([start, end])