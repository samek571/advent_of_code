class Solution:
    def generate(numRows: int):
        if numRows==1: return [[1]]
        elif numRows==2: return [[1],[1,1]]

        cigan=[[1],[1,1],[1,2,1]]
        for i in range (3, numRows): #check for n=3
            temp=[1]
            for o in range(1, len(cigan[-1])):
                temp.append(cigan[-1][o-1]+cigan[-1][o])

            temp.append(1)
            cigan.append(temp)

        return cigan

    print(generate(6))
    print(generate(7))
    print(generate(8))
    print(generate(1))
    print(generate(2))
