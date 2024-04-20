class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # we know these i's wont be fucking flipped
        s = s.rstrip("1").lstrip("0")


        ones = 0; o = 0
        for num in s:

            if num == "1": ones+=1

            elif ones:
                ones-=1 # since we encountered 0
                o+=1

        return o
