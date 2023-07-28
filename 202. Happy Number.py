class Solution:
    def isHappy(n: int) -> bool:
        seen=set()

        while n!=1:
            temp=0
            n=str(n)
            for i in n:
                i=int(i)
                temp+=i*i


            if temp in seen: return False
            seen.add(temp)
            n=temp

        return True

    print(isHappy(19))
    print(isHappy(2))
    print(isHappy(1))