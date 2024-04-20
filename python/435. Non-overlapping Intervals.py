class Solution:
    def eraseOverlapIntervals(self, intervals):# List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        # indexing from 0
        bad, n = 1, len(intervals)

        curr = intervals[0][1]
        for i in range(n):
            if curr <= intervals[i][0]:
                bad+=1
                curr = intervals[i][1]

        return n-bad



def main():
    sol = Solution()
    print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
    print(sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
    print(sol.eraseOverlapIntervals([[1,2],[2,3]]))

if __name__ == "__main__": main()