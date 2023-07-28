class Solution:
    def missingNumber(nums) -> int:
        # #implementing 41. @TODO
        # if len(nums)==1:
        #     if nums[0]==0: return 1
        #     else: return 0
        #
        # n=len(nums)
        # for element in range(n):
        #     index = abs(nums[element])-1
        #     if nums[index] > 0: nums[index] *= -1
        #
        # for i in range(n):
        #     if nums[i] > 0:
        #         return i + 1
        # return n + 1

        # #N log (N)

        # if len(nums) == 1 and nums[0]!=0: return 0
        #
        # #nums.sort()
        # nums=list(set(nums))
        # print([ i for i in range(len(nums)) if nums[i]!=i])
        #
        # # for i in range(len(nums)):
        # #     if nums[i]!=i: return i
        #
        # return len(nums)



        # O(1)
        return len(nums)*(len(nums)+1)//2 - sum(nums)


    print(missingNumber([3,0,1]))
    print(missingNumber([0,1]))
    print(missingNumber([9,6,4,2,3,5,7,0,1]))
    print(missingNumber([0]))
    print("asdasdasd")
    print(missingNumber([1,2,3]))
    print(missingNumber([1]))
    print(missingNumber([0,1,2,3]))
