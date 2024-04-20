from collections import defaultdict

class Solution:
    def minOperations(self, nums, target: int) -> int:
        lenght, summage = len(nums), sum(nums)
        k = summage - target
        if summage == target: return len(nums)

        output, sumcount, dick = 0, 0, {0: -1}
        for idx, num in enumerate(nums):
            sumcount += num
            if sumcount - k in dick:
                output = max(output, idx - dick[sumcount - k])
            dick[sumcount] = idx

        return -1 if output == 0 else lenght - output


def main():
    sol = Solution()
    print(sol.minOperations([10,1,1,1,1,1], 5))
    print(sol.minOperations([1,1], 3))
    print(sol.minOperations([1], 3))
    print(sol.minOperations([3], 3))
    print(sol.minOperations([2,5,20,2,1,3], 7))

    print("\lenght################")
    print(sol.minOperations([3,2,20,1,1,3], target = 10))
    print(sol.minOperations([1,1,4,2,3], target = 5))
    print(sol.minOperations([5,6,7,8,9], target = 4))

if __name__ == "__main__": main()

# lenght, dick, sumcount = len(nums), defaultdict(int), 0
# for idx in range(lenght - 1, lenght // 2 - 1, -1):
#     sumcount += nums[idx]
#     dick[lenght - idx] = sumcount
#     if dick[lenght - idx] == target or sumcount == target: return lenght - idx
#
# sumcount, output = 0, float("inf")
# for i, num in enumerate(nums):
#     if i == lenght // 2 + 1: break
#
#     sumcount += i
#
#     if target - sumcount in dick or sumcount == target:
#         output = min(dick[target - sumcount] + i, output)
#
#     elif sumcount > target:
#         return -1
#
# return output

"""
lenght, dick, sumcount, output = len(nums), defaultdict(int), 0, len(nums)+1

        tmp = min(nums[-1],nums[0])
        if tmp > target: return -1
        elif tmp == target: return 1

        if lenght == 1: return 1 if nums[0]==target else -1
        elif lenght == 2:
            if target == sum(nums): return 2
            else: return -1


        for Ridx in range(lenght-1, -1, -1):
            sumcount += nums[Ridx]
            dick[sumcount] = lenght-Ridx

            if sumcount == target: output = min(output, lenght-Ridx)
            elif sumcount > target: break

        sumcount = 0
        for Lidx, left in enumerate(nums):

            sumcount += left
            right = target-sumcount
            if right in dick or sumcount == target:
                 output = min(output, dick[right]+Lidx+1, sumcount)

        return -1 if output == lenght+1 else output
"""