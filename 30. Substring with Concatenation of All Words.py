from collections import Counter
class Solution:
    def findSubstring(s: str, words):
        # step=len(words[0])
        # totallenght=step*len(words)
        # index=0
        # outputlist=[]
        #
        #
        # if totallenght>len(s) or len(s)<step: return []
        #
        # while index+totallenght<=len(s):
        #     copi=words.copy()
        #     potential_output=index
        #
        #     while s[index:index+step] in copi:
        #         copi.remove(s[index:index+step])
        #         index+=step
        #
        #     if len(copi)==0:
        #         outputlist.append(potential_output)
        #
        #     index = potential_output +1
        #
        # return outputlist

        step=len(words[0])
        totalLenght=step*len(words)
        index=0
        returnList=[]


        if totalLenght>len(s) or len(s)<step: return []

        while index+totalLenght<=len(s):
            dictionary=Counter(words)
            potential_output=index

            while len(dictionary)>0:
                dictionary[s[index:index+step]]-=1
                if dictionary[s[index:index+step]]==0: del (dictionary[s[index:index+step]])
                elif dictionary[s[index:index+step]]<0: break
                index+=step

            if len(dictionary)==0:
                returnList.append(potential_output)

            index = potential_output +1

        return returnList

    print(findSubstring("agfagasdgergegaskijwebagahfuysdbvsaygca", ["a", "g"]))
    print(findSubstring("aaaaaaaaygcaaa", ["aa"]))
    print(findSubstring("agfaasdgergegskijwebhfuysdbvsaygca", ["a"]))
    print(findSubstring("agfaasdgergegskijagagwebhfuysdbvsagygca", ["ag"]))
    print(findSubstring("agfaasdgergegskijaghagaghwebhfuysdbvsagygca", ["agh"]))
    print(findSubstring("aghaghagaghwebhfuysdbvsagygca", ["agh"]))

    print("\n")
    print(findSubstring("barfoothefoobarman", words = ["foo","bar"]))
    print(findSubstring("wordgoodgoodgoodbestword", words = ["word","good","best","word"]))
    print(findSubstring("barfoofoobarthefoobarman", words = ["bar","foo","the"]))
