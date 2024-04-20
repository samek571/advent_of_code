class Solution:
    def maxSumDivThree(nums) -> int:
        mod1=[float('inf')]
        mod2=[float('inf')]

        totale=0
        for i in nums:
            totale+=i
            if i%3 == 1: mod1.append(i)
            elif i%3 == 2: mod2.append(i)


        if totale%3==0: return totale

        mod2.sort()
        mod1.sort()
        if totale%3==1: return totale - min(sum(mod2[:2]), mod1[0])
        elif totale%3==2: return totale - min(sum(mod1[:2]), mod2[0])


    print(maxSumDivThree([3,6,5,1,8]))
    print(maxSumDivThree([3]))
    print(maxSumDivThree([4]))
    print(maxSumDivThree([1,2,3,4,4]))
    print(maxSumDivThree([1,2,3]))