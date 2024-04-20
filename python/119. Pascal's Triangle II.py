class Solution:
    def getRow(rowIndex):
        rowIndex+=1
        if rowIndex==1: return [1]
        elif rowIndex==2: return [1,1]

        cigan=[[1,2,1]]
        for i in range (3, rowIndex):
            temp=[1]
            for o in range(1, len(cigan[-1])):
                temp.append(cigan[-1][o-1]+cigan[-1][o])

            temp.append(1)
            cigan[-1]=temp

        return cigan[-1]

    print(getRow(6))
    print(getRow(7))
    print(getRow(8))
    print(getRow(1))
    print(getRow(2))
    print(getRow(0))
