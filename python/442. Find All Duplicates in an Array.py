class Solution:
    def findDuplicates(nums):
        # k=len(nums)
        #
        # #edge cases
        # if k==1: return []
        # elif k==2:
        #     if nums[0]==nums[1]: return [nums[0]]
        #     else: return []
        #
        # #
        # number_of_edge_elements=0
        # for i in range(k):
        #     if nums[i]==k:
        #         nums[i]=0
        #         number_of_edge_elements+=1
        #
        # #magic
        # counter=0
        # for i in range(k):
        #     if nums[abs(nums[i])] >= 0:
        #         nums[abs(nums[i])] *= -1
        #     else:
        #         nums.append(abs(nums[i]))
        #         counter+=1
        #         if abs(nums[i]) == 0:
        #             index=counter-1
        #
        # if max(nums)==0:
        #     return []
        #
        # if number_of_edge_elements>1:
        #     nums[index+k] = k
        # return nums[-counter:]

        result = []
        k = len(nums)

        for i in range(k):
            id = (nums[i] % k) - 1
            nums[id] += k

        for i in range(k):
            if nums[i] > 2 * k:
                result.append(i + 1)

        return result


# first is so far working for at least one duplicate, not for none
    print(findDuplicates([10,2,5,10,9,1,1,4,3,7]))
    print(findDuplicates([7, 6, 2, 3, 4, 1, 5, 9, 9, 8, 7, 10, 11]))
    print(findDuplicates([7,6,2,3,4,1,5,8,8]))
    print(findDuplicates([2,2]))
    print(findDuplicates([4,3,2,2,3,1,4,9,9]))
    print(findDuplicates([4,3,2,7,8,2,3,1]))
    print(findDuplicates([4, 3, 2, 2, 3, 1, 9, 9, 6]))
    print(findDuplicates([1,1,2]))
    print(findDuplicates([1]))
    print(findDuplicates([1,2,3,4,5,6]))
    print(findDuplicates([6,2,3,4,1,5,7]))

