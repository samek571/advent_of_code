class Solution:
    def tupleSameProduct(nums) -> int:
        table=dict()

        for a in range(0,len(nums)):
            for b in range(a+1, len(nums)):
                x=nums[a] * nums[b]
                if x in table: table[x]+=1
                else: table[x]=1

        output=0
        for val in table.values():
            output+=4*val*(val-1)

        return output


    print(tupleSameProduct([2,3,4,6]))
    print(tupleSameProduct([1,2,4,5,10]))
    print(tupleSameProduct([2,3,4,6,8,12]))
    print(tupleSameProduct([2,3,5,7]))
    print(tupleSameProduct([]))
    print(tupleSameProduct([1,2,3]))
    print(tupleSameProduct([1,2,3,6]))
