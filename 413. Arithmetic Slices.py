class Solution:
    def numberOfArithmeticSlices(nums) -> int:
        n = len(nums)

        if n < 3: return 0

        total, k, distance = 0, 2, nums[1] - nums[0]

        for i in range(2, n):
            diferenciacia = nums[i]-nums[i-1]

            if diferenciacia == distance: k+=1
            else:
                if k>2: total+= (k*(k-2)) - (((k-1)*k)//2)+1

                distance = diferenciacia
                k = 2

        if k > 2: total += (k * (k - 2)) - (((k - 1) * k) // 2) + 1
        return total

    print(numberOfArithmeticSlices([1,2,3,4,5,6,7]))