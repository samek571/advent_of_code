import math
class Solution:
    def maxNumberOfBalloons(text) -> int:

        dick={"b":0, "a":0, "l":0, "o":0, "n":0}

        for i in range(len(text)):
            if text[i]=="b" or text[i]=="a" or text[i]=="n":
                dick[text[i]]+=1
            elif  text[i]=="l" or text[i]=="o" :
                dick[text[i]]+=0.5

        print(dick)
        return math.floor(min(dick.values()))


    print(maxNumberOfBalloons("balloonsballoonjhasballoonaidballooniasodijaosdjbaaaallooaoasasdasdballoon"))