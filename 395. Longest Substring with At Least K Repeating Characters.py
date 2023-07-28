
from collections import Counter
@lru_cache(None)

def longestSubstring(s: str, k: int) -> int:

    for char, count in Counter(s).items():
        if count < k: return max(longestSubstring(s, k) for s in s.split(char))
    return len(s)


print(longestSubstring("iiisjdfbhiusdfhbfqwn", 2))                  #3
print(longestSubstring("iiisjdfbhiusdfhbjhwdbfjhdbfjksdffqwn", 5))  #0
print(longestSubstring("isdfkjhbsdfkiisjdfbhiusdfhbfqwn", 4))       #0
print(longestSubstring("aaabb",3))                                  #3
print(longestSubstring("ababbc",2))                                 #2

        ##zle pochopene zadanie...

        # hovienko={}
        # letters=set()
        #
        # for i in range(len(s)):
        #     if s[i] in hovienko:
        #         hovienko[s[i]]+=1
        #         if  hovienko[s[i]]==k: letters.add(s[i])
        #     else: hovienko[s[i]]=1
        #
        # if len(letters)==0: return 0

        # output=0
        # i=0
        # while i<len(s):
        #     if s[i] in letters:
        #         iter=i
        #         counter=0
        #         while s[iter] in letters:
        #             iter+=1
        #             counter+=1
        #
        #         output=max(counter,output)
        #         i=iter
        #
        #     i+=1
        # return output
