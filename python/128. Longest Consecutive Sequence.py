class Solution:
    def longestConsecutive(nums) -> int:
        setaz=set(nums)
        counter=output=0

        for number in nums:

            if number-1 in setaz: continue
            #forcing start of the potential c. seq to go from the lowest element

            while number+counter in setaz: counter+=1
            output=max(counter,output)
            counter=0

        return max(counter, output)

    print(longestConsecutive([1,2,3,4,6,7]))
    print(longestConsecutive([]))

