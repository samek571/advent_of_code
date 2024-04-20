class Solution:
    def evalRPN(tokens) -> int:
        array=[]

        i=0
        while i < len(tokens):
            if tokens[i] == "-":
                number = int(array[-2]) - int(array[-1])
                array.pop()
                array.pop()
                array.append(number)
            elif tokens[i] == "+":
                number = int(array[-2]) + int(array[-1])
                array.pop()
                array.pop()
                array.append(number)
            elif tokens[i] == "*":
                number = int(array[-2]) * int(array[-1])
                array.pop()
                array.pop()
                array.append(number)
            elif tokens[i] == "/":
                number = int(array[-2]) / int(array[-1])
                array.pop()
                array.pop()
                array.append(number)

            else:
                array.append(tokens[i])

            i+=1

        return int(array[0])

    #print(evalRPN(["4","13","5","/","+"]))
    #print(evalRPN(["2","1","+","3","*"]))
    print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))