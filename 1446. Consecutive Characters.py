

class Solution:
    def maxPower(s: str):
        maks=counter=1
        for i in range(1, len(s)):
            if s[i-1]==s[i]:
                counter+=1
                maks = max(maks, counter)
            else:
                counter=1

        return maks
    print(maxPower("aayzzzzzzzz"))
    print(maxPower("triplepillooooow"))
    print(maxPower("hooraaaaaaaaaaay"))
    print(maxPower("hovno"))
    print(maxPower("hooovno"))
    print(maxPower("abbcccddddeeeeedcba"))
    print(maxPower("cc"))
    print(maxPower("c"))
