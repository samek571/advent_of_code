class Solution:
    def threeSum(nums, target):
        if len(nums)<4:
            return []

        nums=sorted(nums)
        output=[]
        for z in range(len(nums)-2):
            for a in range(z,len(nums)-2):

                b=a+1
                c=len(nums)-1
                while b<c:
                    if nums[z] + nums[a] + nums[b] + nums[c] == target and\
                            [nums[z], nums[a],nums[b],nums[c]] not in output and\
                            a!=z!=b!=c:
                        output.append([nums[z], nums[a],nums[b],nums[c]])
                        b+=1
                    elif nums[z] + nums[a] + nums[b] + nums[c] < target:
                        b+=1
                    else:
                        c-=1

        return output

    print(threeSum([1,0,-1,0,-2,2], target = 0))
    print(threeSum([2,2,2,2,2], target = 8))
    print(threeSum([1,2,3,1,2,3,0,0], 6))