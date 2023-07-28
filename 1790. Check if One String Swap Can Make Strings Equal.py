class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n=len(s1)

        if n<=2:
            return Counter(s1) == Counter(s2)

        h=0
        for i in range(len(s1)):
            if s1[i] != s2[i]: h+=1
        
        return not h>2 and  Counter(s1) == Counter(s2)
