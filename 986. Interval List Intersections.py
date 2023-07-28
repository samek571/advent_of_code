class Solution:
    def intervalIntersection(firstList, secondList):
        len(secondList)

        i=0
        output=[]

        for i1 in firstList:
            for i2 in secondList[i:len(secondList)]:
                if i2[0] > i1[1]: break
                elif i1[0] > i2[1]:
                    i+=1
                    continue

                output += [[max(i1[0], i2[0]), min(i2[1],i1[1])]]

        return output

    print(intervalIntersection([[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]))