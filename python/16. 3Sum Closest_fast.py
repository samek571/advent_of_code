class Solution:
    def threeSumClosest(nums, target: int) -> int:
        # if len(nums)<=3:
        #     return sum(nums)
        #
        # nums=sorted(nums)
        # print(nums, target)
        # smallest_deviation=nums[0]+nums[1]+nums[-1]
        #
        # for a in range(len(nums)-2):
        #     for b in range(a+1, len(nums)-1):
        #         c=len(nums)-1
        #
        #         while b!=c:
        #             sumaz = nums[a] + nums[b] + nums[c]
        #
        #             if sumaz == target:
        #                 return sumaz
        #
        #             if abs(smallest_deviation-target) > abs(sumaz-target):
        #                 smallest_deviation=sumaz
        #             c-=1
        #
        # return smallest_deviation

        if len(nums)<=3:
            return sum(nums)

        nums=sorted(nums)
        print(nums, target)
        smallest_deviation=nums[0]+nums[1]+nums[-1]

        for a in range(len(nums)-1):
            b=a+1
            c=len(nums)-1

            while b<c:
                sumaz = nums[a] + nums[b] + nums[c]

                if sumaz == target:
                    return sumaz

                if abs(smallest_deviation-target) > abs(sumaz-target):
                    smallest_deviation=sumaz

                if sumaz>target:
                    c-=1
                else:
                    b+=1

        return smallest_deviation

    print(threeSumClosest([-1,2,1,-4],1))
    print(threeSumClosest([-1,-2,1,-4],1))
    print(threeSumClosest([-1,-1,-2,1,-4],1))
    print(threeSumClosest([-4,3,7,5,67,4,11],8))
    print(threeSumClosest([3,7,5,67,4,11],8))
    print(threeSumClosest([3,7,5,67,4,11],811))
    print(threeSumClosest([0,0,0],4))

'''
[-1,2,1,-4]
1
[0,0,0]
1
[3,7,5,67,4,11]
811
[3,7,5,67,4,11]
8
[-4,3,7,5,67,4,11]
8
[-1,-1,-2,1,-4]
1
[-1,2,1,-4]
1
[-1,-2,1,-4]
1
'''