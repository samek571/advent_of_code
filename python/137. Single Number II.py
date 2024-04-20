class Solution:
    def singleNumber(nums) -> int:
        return (3 * sum(set(nums)) - sum(nums))//2

    print(singleNumber([2,2,2,3]))
    print(singleNumber([0,1,0,1,0,1,99]))
    print(singleNumber([5,5,5,9,2,2,2,10,10,10])) #60, 26, 4, 10