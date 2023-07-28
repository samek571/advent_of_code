def letterCombinations(digits: str):

    if len(digits)==0: return []

    output=[]
    hashm= {2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l'], 6:['m','n','o'],
                  7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z']}

    if len(digits)==1:
        return hashm[int(digits)]

    else:
        for i in range (len(digits)):
            maslo=hashm[int(digits[i])]
            chleba=letterCombinations(digits[i+1:])

            for one in maslo:
                for second in chleba:
                    output.append(one+second)

            print(maslo)

            return output

print(letterCombinations("427"))
        # if len(digits)==0:
        #     return []
        #
        # combs=[]
        # if len(digits)==1:
        #     var=hovno[digits[0]]
        #     for i in range(len(hovno[int(digits[0])])):
        #         combs.append(hovno[i])
        #
        # return combs

