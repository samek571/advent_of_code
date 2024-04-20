from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str):# -> List[int]:
        ls, lp = len(s), len(p)
        if ls<lp: return []


        o, alpha = [], Counter(p)
        for i in range(ls-lp+1):
            hsh = Counter(s[i:lp+i])

            if hsh == alpha: o+=[i]

        return o

# first "must implement" is to do it via while cycle and if we encounter an element that has no
# use in the anagram (p) --> automatically i+=len(p) because its presence already disgusted len(p) steps

# second: just removing s[i] element from the hashmap and adding s[i+len(p)]
# i.e not making new hashmap everytime


def main():
    sol = Solution()
    print(sol.findAnagrams(s = "abab", p = "ab"))
    print(sol.findAnagrams(s = "cbaebabacd", p = "abc"))
    print(sol.findAnagrams(s = "a", p = "abc"))
    print(sol.findAnagrams(s = "acb", p = "abc"))

if __name__ == "__main__": main()