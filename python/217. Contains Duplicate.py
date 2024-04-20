class Solution:
    def containsDuplicate(nums) -> bool:
        hovno=set()

        for i in nums:
            if i in hovno:
                return True
            else:
                hovno.add(i)
        return False

    print(containsDuplicate([1,2,4,5]))
    print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
    print(containsDuplicate([1,2,3,4]))
    print(containsDuplicate([1,2,3,1]))