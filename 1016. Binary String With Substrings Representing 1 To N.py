class Solution:
    def queryString(s: str, n: int) -> bool:
        for i in range(1,n+1):
            if bin(i)[2:] not in s:
                return False
        return True

    print(queryString("0110", 3))