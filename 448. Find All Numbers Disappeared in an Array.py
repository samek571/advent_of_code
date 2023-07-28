class Solution:
    def findDisappearedNumbers(nums):
        setaz = set(i for i in range(1, len(nums)+1))

        return list(setaz-set(nums))

    print(findDisappearedNumbers([1,3,3,4,5,5,6,6]))