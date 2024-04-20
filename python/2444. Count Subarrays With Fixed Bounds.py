import bisect
from collections import deque

class Solution:
    '''
    if min=max it is different problem, its implementation is pretty easy

    - since this is sort of sliding window algo, it doesnt matter if we are out of
    higher or the lower bond since we have to have both in there simultaneosly
    - lets note down the elements in arr that are out of the plausible interval
    we end up getting some smaller sub-problems
    -in each subproblem there is somewhere in the stream of numbers min and max;
    there is this nlogn algo that gets it correct

    the current implementation has O(nlogn) which is okay but it could be better by
    making dequeues from the lists and leftpoping and doing math

    The time complexity of this code is O(n), where n is the length of the input list nums.
    The outer loop iterating over the nums list takes O(n) time, and the getRes function takes O(n) time as well.
    So, the total time complexity is O(n) + O(n) = O(n).
    '''


    def getRes(self, nums, si, ei, minK, maxK):
        mink = deque()
        maxk = deque()
        for i in range(si, ei + 1):
            if nums[i] == minK:
                mink.append(i)
            if nums[i] == maxK:
                maxk.append(i)

        res = 0
        i = si
        while i <= ei:
            while mink and mink[0] < i:
                mink.popleft()
            while maxk and maxk[0] < i:
                maxk.popleft()
            if not mink or not maxk:
                i += 1
                continue
            x = mink[0]
            y = maxk[0]
            v = max(x, y)
            res +=  (ei - v + 1)
            i += 1

        return res



    def countSubarrays(self, nums, minK: int, maxK: int) -> int:

        if minK == maxK:
            nums.append(minK+1)

            total = 0; curr = 0
            for i in nums:

                if i == minK:
                    curr += 1
                else:
                    total += ((curr + 1) * curr) // 2
                    curr = 0

            return total

        l, r = -1, -1
        ans = 0
        for i in range(len(nums)):
            if minK <= nums[i] <= maxK:
                if l == -1:
                    l = i
                r = i
            else:
                if l != -1:
                    ans += self.getRes(nums, l, r, minK, maxK)
                    l = -1
                    r = -1
            if minK <= nums[i] <= maxK:
                if l == -1:
                    l = i
                r = i
        if l != -1:
            ans += self.getRes(nums, l, r, minK, maxK)

        return ans





def main():
    sol = Solution()
    print(sol.countSubarrays([3,3,1,3,3,5,3,1,5,3], 1, 5))
    print(sol.countSubarrays([3,3,1,3,3,5,3,1,5,3,3], 1, 5))
    print(sol.countSubarrays([1,1,1,1,7,1,1], 1, 1))
    print(sol.countSubarrays([1,1,1,1,1,1], 1, 1))
    print(sol.countSubarrays([1,1,1,1,1], 1, 1))
    print(sol.countSubarrays([1,1,1,1], 1, 1))
    print(sol.countSubarrays([1,1], 1, 1))

if __name__ == "__main__": main()
