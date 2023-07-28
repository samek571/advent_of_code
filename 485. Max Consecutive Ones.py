class Solution:
    def findMaxConsecutiveOnes(nums) -> int:
        highest=0
        counter=0
        i=0
        for i in nums:
            if i==1:
                counter+=1
            else:
                if counter>highest:
                    highest=counter
                counter=0

        if highest > counter: return highest
        else: return counter
    print(findMaxConsecutiveOnes([1,1,1,0,1,1,1,1,0,1,0,1]))