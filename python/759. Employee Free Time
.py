
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

#it is clear that we need some sort of sorted ds, easiest it is with sorted list; logn is insertion and there are k intervals, so complexity is within the norm. intervals get inserted one by one and if something like this happens 
#[3,7], [4,10] --> arr[i][1] > arr[i+1][0] --> [i,max(arr[i][1], arr[i+1][1])]
#^ this should be done everytime so we dont have unecesarry big list 

#some obvious sorted arr / heapq
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':

        intervals = []
        for employee_schedule in schedule:
            for interval in employee_schedule:
                intervals.append((interval.start, interval.end))
        
        intervals.sort()


        merged_intervals = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= merged_intervals[-1][1]:
                merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], interval[1]))
            else:
                merged_intervals.append(interval)
        

        free_time = []
        for i in range(1, len(merged_intervals)):
            start = merged_intervals[i-1][1]
            end = merged_intervals[i][0]
            free_time.append(Interval(start, end))
        
        return free_time
