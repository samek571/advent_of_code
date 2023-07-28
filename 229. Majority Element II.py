class Solution:
    def majorityElement(nums):
        # O(n) and O(n)
        hesmabp = dict()

        for i in nums:
            if i not in hesmabp:
                hesmabp[i] = 1
            else:
                hesmabp[i] += 1

        output=[]
        for key, val in hesmabp.items():
            if val>len(nums)//3:
                output.append(key)
                if len(output)==2: return output

        return output

    print(majorityElement([3, 1, 1, 3, 6]))
    print(majorityElement([3, 2, 3]))
    print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
    print(majorityElement([5]))
    print(majorityElement([5,4,1,0,1,4,5]))
    print(majorityElement([3, 3, 3, 3, 3, 99]))