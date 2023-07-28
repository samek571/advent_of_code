class Solution:
    def busyStudent(startTime, endTime, queryTime: int) -> int:

        # for i in range(len(startTime)-1):
        #     if startTime[i]>queryTime or endTime[i]<queryTime:
        #         startTime[i]="#"
        #
        # counter=0
        # for i in startTime:
        #     if i != "#": counter+=1
        #
        # return counter

        counter=0
        for i in range(len(startTime)):
            if (startTime[i]<=queryTime) and (endTime[i]>=queryTime): counter+=1

        return counter


    print("\ndobre")
    print(busyStudent([4], endTime = [4], queryTime = 4))
    print(busyStudent([9,8,7,6,5,4,3,2,1], endTime = [10,10,10,10,10,10,10,10,10], queryTime = 5))
    print(busyStudent([1,2,3], endTime = [3,2,7], queryTime = 4))

    print(busyStudent([1,1,1,1], endTime = [1,3,2,4], queryTime = 7))
    print(busyStudent([4], endTime = [4], queryTime = 5))
    print(busyStudent([4], endTime = [4], queryTime = 3))
