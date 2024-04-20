class Solution:
    def moveZeroes(nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=len(nums)-1
        counter=0

        while i>-1:
            if nums[i]==0:
                nums.pop(i)
                counter+=1

            i-=1
        nums.extend([0]*counter)
        return nums
    print(moveZeroes([0,1,2,0,7,0,2,5]))

# cez swapy to je lepsie