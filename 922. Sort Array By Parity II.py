class Solution:
    def sortArrayByParityII(nums):
        outputlist=[]

        even=[]
        odd=[]

        for i in nums:
            if i%2==0 and len(outputlist)%2==0:
                outputlist.append(i)
            elif i%2==1 and len(outputlist)%2==1:
                outputlist.append(i)
            elif i%2==0 and len(outputlist)%2==1:
                even.append(i)
                if len(odd)>0:
                    outputlist.append(odd[-1])
                    odd.pop()
            else:
                odd.append(i)
                if len(even)>0:
                    outputlist.append(even[-1])
                    even.pop()

        while (len(odd)!=0) or (len(even)!=0):
            if outputlist[-1]%2==0 and len(odd)>0:
                outputlist.append(odd[-1])
                odd.pop()
            elif outputlist[-1]%2==1 and len(even)>0:
                outputlist.append(even[-1])
                even.pop()

        return outputlist

    print(sortArrayByParityII([3,1,4,2]))
    print(sortArrayByParityII([3,9,0,0]))
    print(sortArrayByParityII([4,2,5,7]))
    print(sortArrayByParityII([2,3]))
    print(sortArrayByParityII([5,4,3,3,3,2,2,9,8,8]))
