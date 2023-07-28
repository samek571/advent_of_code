class Solution:
    def merge(intervals):
        intervals.sort(key=lambda x: x[0])
        merged=[intervals[0]]

        for i in intervals[1:]:
            if  merged[-1][-1] >= i[0]:  merged[-1][-1] = max(merged[-1][-1], i[-1])
            else: merged.append(i)

        return merged

    print(merge([[1,3],[4,5], [5,6], [6,999], [0,25]]))

    print(merge([[1,3],[2,6],[15,18],[8,10]]))
    print(merge([[1,4],[4,5]]))
    ##########
    print(merge([[1,3],[4,5], [5,6], [7,999]]))
