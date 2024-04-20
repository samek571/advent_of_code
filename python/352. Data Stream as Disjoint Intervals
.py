class SummaryRanges:
    def __init__(self):
        self.arr = []



    def addNum(self, val: int) -> None:
        e=[val,val]
        index = bisect.bisect_left(self.arr, e)
        
        if index > 0 and self.arr[index - 1][1] + 1 >= e[0]:
            self.arr[index - 1][1] = max(self.arr[index - 1][1], e[1]) #yes the max is necesarry
            
            # Check if merging is possible with the next interval 
            if index < len(self.arr) and self.arr[index - 1][1] + 1 >= self.arr[index][0]:
                self.arr[index - 1][1] = max(self.arr[index - 1][1], self.arr.pop(index)[1])
        

        # If the interval to be inserted is overlapping with the next interval, merge them
        elif index < len(self.arr) and self.arr[index][0] - 1 <= e[1]:
            self.arr[index][0] = min(self.arr[index][0], e[0])
            self.arr[index][1] = max(self.arr[index][1], e[1])


        else:
            self.arr.insert(index, e)




    def getIntervals(self) -> List[List[int]]:
        return self.arr


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
