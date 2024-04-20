import collections

class Solution:
    def findRepeatedDnaSequences(self, s: str):# -> List[str]:
        if len(s)<10: return []

        hsh = collections.defaultdict(int)

        for i in range(len(s)-9):
            hsh[s[i:i+10]] +=1

        o = []
        for key, val in hsh.items():
            if val > 1: o.append(key)

        return o



def main():
    sol = Solution()
    print(sol.findRepeatedDnaSequences('AAAAAAAAAAAAA'))
    print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

if __name__ == "__main__": main()
