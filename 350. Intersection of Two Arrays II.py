class Solution:
    def intersect(nums1, nums2):
        nums1.sort()
        nums2.sort()

        output=[]
        x=y=0   #pointers
        while x<len(nums1) and y<len(nums2):

            #staying in here till something fucks up
            if nums2[y]==nums1[x]:
                output.append(nums1[x])
                x,y = x+1, y+1
                continue

            #fuckup: values are not equal
            else:

                #nums2 moved lvl up
                if nums2[y]>nums1[x]:
                    while nums2[y]>nums1[x]:
                        x+=1
                        if x==len(nums1): return output

                #nums1 moved lvl up
                else:
                    while nums2[y]<nums1[x]:
                        y+=1
                        if y==len(nums2): return output

        return output

    print(intersect([3,2],[1,9]))
    print(intersect([],[]))
    print(intersect([1,2,2,1], nums2 = [2,2]))
    print(intersect([4,9,5], nums2 = [9,4,9,8,4]))