class Solution:
    def productExceptSelf(nums):
        product=1
        output=[]
        multiplying_by_zero=0

        for i in nums:
            if not i==0:
                product*=i
            else:
                multiplying_by_zero+=1
                if multiplying_by_zero>1:
                    return [0]*len(nums)

        if multiplying_by_zero==0:
            for i in nums:
                output.append(int(product/i))

        elif multiplying_by_zero==1:
            for i in nums:
                if i==0:
                    output.append(product)
                else:
                    output.append(0)

        return output

    print(productExceptSelf([-1,1,0,-3,3]))
    print(productExceptSelf([1,2,3,4]))
