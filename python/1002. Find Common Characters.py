class Solution:
    def commonChars(words):
        # table=dict()
        # for letter in words[0]:
        #     if letter in table: table[letter]+=1
        #     else: table[letter]=1
        #
        # for word_idx in range(1, len(words)-1):
        #     for letter in words[word_idx]:
        #         if letter in table: table[letter]+=1
        #
        #     dict

        output=list(words[0])
        for word in words[1:]:
            temp = []
            for ch in output:
                if ch in word:
                    temp.append(ch)
                    word = word.replace(ch, "*", 1)
            output = temp
        return output


    print(commonChars(["hovno", "abcn"]))
    print(commonChars(["abcn"]))
    print(commonChars(["bella","label","roller"]))
    print(commonChars(["cool","lock","cook"]))
