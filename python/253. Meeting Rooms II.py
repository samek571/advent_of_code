class Solution:
    def minMeetingRooms(self, intervals) -> int:
        #improved with heap
        # we only store end times. We iterate through each and every interval -
        # 1) if start of some is more than end of any in the heap --> pop
        # 2) append new
        # 3) loook at the size of heap



        stream = []
        for e in intervals:
            stream.append([e[0], 1]); stream.append([e[-1], -1])

        #doesnt work for some reason
        #stream = [[e[0], 1]; [e[-1], -1] for e in intervals]

        cnt, res, stream = 0, 0, sorted(stream)
        for info in stream:
            if info[1] == 1:
                cnt+=1
                res = max(res, cnt)
            else:
                cnt-=1

        return res



def main():
    sol = Solution()
    print(sol.minMeetingRooms([[0,30],[5,10],[15,20]]))
    print(sol.minMeetingRooms( [[7,10],[2,4]]))

if __name__ == "__main__": main()