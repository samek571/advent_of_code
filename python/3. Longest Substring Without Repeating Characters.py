class Solution:
    def lengthOfLongestSubstring(s) -> int:
        seen=dict()
        i=output=counter=0

        while i<len(s):
            if s[i] not in seen:
                seen[s[i]]=i
                counter+=1
            else:
                if counter>output:
                    output=counter
                collision=seen[s[i]]

                number_of_deleted=0
                for key in list(seen.keys()):
                    if seen[key]<=collision:
                        del seen[key]
                        number_of_deleted+=1
                    else: break

                seen[s[i]] = i
                counter-=(number_of_deleted-1)
            i+=1

        print(seen)

        if counter > output: return counter
        else: return output

    print(lengthOfLongestSubstring("hovnopenisoabcdefg"))   #11
    print(lengthOfLongestSubstring("c"))        #1
    print(lengthOfLongestSubstring("au"))       #2
    print(lengthOfLongestSubstring("hovno"))    #4
    print(lengthOfLongestSubstring("dvdf"))     #3
    print(lengthOfLongestSubstring("aab"))      #2
    print(lengthOfLongestSubstring("pwwkew"))   #3
    print(lengthOfLongestSubstring("abcabcbb")) #3
    print(lengthOfLongestSubstring(" "))        #1
    print(lengthOfLongestSubstring(""))         #0
