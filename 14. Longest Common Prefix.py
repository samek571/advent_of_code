class Solution:
    def longestCommonPrefix(strs):
        output=strs[0]
        for i in range(1,len(strs)):
            if len(output)==0:
                return ""

            y=0
            while (y<len(strs[i]) and y<len(output)) and (strs[i][y]==output[y]):
                y+=1

            output = strs[i][:y]

        return output



    print(longestCommonPrefix(["cigan", "cicka", "cic"]))
    print(longestCommonPrefix(["abcd", "abc", "ab"]))
    print(longestCommonPrefix(["dog","racecar","car"]))
    print(longestCommonPrefix(["flower","floow","flight"]))
    print(longestCommonPrefix(["flower"]))
