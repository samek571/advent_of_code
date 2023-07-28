import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1) ; desired = collections.Counter(s1)
        curr = collections.defaultdict(int)
        for num in s2[:n]: curr[num] += 1
        print(curr)


        if curr == desired: return True
        for char_idx in range(n, len(s2)):
            curr[s2[char_idx-n]] -= 1
            curr[s2[char_idx]] += 1

            if curr[s2[char_idx-n]] == 0: curr.pop(s2[char_idx-n])
            if curr == desired: return True

        return False

def main():
    sol = Solution()
    print(sol.checkInclusion(s1 = "ab", s2 = "eidbaooo"))
    print(sol.checkInclusion(s1 = "ab", s2 = "eidboaoo"))

if __name__ == "__main__": main()