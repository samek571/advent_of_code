class Solution:
    def checkPossibility(nums) -> bool:
        warning=0
        i=0
        if len(nums) < 3:
            return True

        while len(nums) > i+2:
            #123 ideal
            if nums[i]<=nums[i+1]<=nums[i+2]:
                i+=1
                continue
            #321 you had one job
            elif (nums[i] > nums[i+1] and nums[i+1] > nums[i+2]):
                return False

            #first digit 211 212 213 311 312 313 322 323
            elif (nums[i]>nums[i+1] and nums[i+1]<=nums[i+2]):
                warning+=1
                i+=1
            #second digit 121 131 132 232 ok
            elif (nums[i]<=nums[i+2] and nums[i+1]>nums[i+2]):
                warning+=1
                nums[i+1]=nums[i]
                i+=1
            #third digit 231 331 332 ok
            elif (nums[i]<=nums[i+1] and nums[i+1]>nums[i+2]):
                warning+=1
                nums[i+2]=nums[i+1]
                i+=1

            if warning > 1:
                return False
        return True

    print(checkPossibility([-1,4,2,3])) #true
    print(checkPossibility([2,3,3,2,2])) #false
    print(checkPossibility([4, 2, 1]))
    print("hovno")
    print(checkPossibility([3, 2, 1]))
    print(checkPossibility([3, 1, 2]))
    print(checkPossibility([2, 1, 3]))
    print(checkPossibility([2, 3, 1]))
    print(checkPossibility([1, 2, 3]))
    print(checkPossibility([1, 3, 2]))