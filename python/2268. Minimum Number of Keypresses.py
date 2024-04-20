import collections

class Solution:
    def minimumKeypresses(self, s: str) -> int:
        h = [0]*26

        for i in s:
            h[ord(i)-97] += 1

        h = sorted(h, reverse=True)
        print(h)
        return sum(h[:9]) + 2*sum(h[9:18]) + 3*sum(h[18:])


def main():
    sol = Solution()
    print(sol.minimumKeypresses("abcdefghijkl"))
    print(sol.minimumKeypresses("apple"))
    print(sol.minimumKeypresses("abcdefghijkzl"))

if __name__ == "__main__": main()


