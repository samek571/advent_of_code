class Solution:
    def find132pattern(nums) -> bool:
        n=len(nums)
        if n<3: return False
        mi = [nums[0]]
        stack=[]

        for i in range(1,n): mi.append( min(mi[-1], nums[i]) )

        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=mi[i]: stack.pop()

            if stack and mi[i] < stack[-1] < nums[i]: return True

            stack.append(nums[i])
        return False

    print(find132pattern([5,2,3,4,6,5]))
    print(find132pattern([1,2,3,4,6,5]))
    print(find132pattern([2,4,6,1]))
