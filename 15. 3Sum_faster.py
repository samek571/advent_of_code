class Solution:
    def threeSum(nums):
        if len(nums)<3:
            return []

        nums=sorted(nums)
        output=[]

        for a in range(len(nums)-2):
            b=a+1
            c=len(nums)-1
            while b<c:
                if nums[a]+nums[b] + nums[c] ==0 and [nums[a],nums[b],nums[c]] not in output:
                    output.append([nums[a],nums[b],nums[c]])
                    b+=1
                elif nums[a]+nums[b] + nums[c] <0:
                    b+=1
                else:
                    c-=1

        return output
    print(threeSum([-1,0,1,2,-1,-4]))
    print(threeSum([-1,0,1,2,-1,-2]))
    print(threeSum([1,0,-1]))
