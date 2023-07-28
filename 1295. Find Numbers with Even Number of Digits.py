class Solution:
    def findNumbers(nums) -> int:
        counter=0

        for i in nums:
            i=str(i)
            if len(i)%2==0: counter+=1

        return counter



    print(findNumbers([12,345,2,6,7896]))
    print(findNumbers([555,901,482,1771]))