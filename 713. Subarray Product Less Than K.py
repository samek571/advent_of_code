class Solution:
    def numSubarrayProductLessThanK(self, nums, target: int) -> int:
        product, i, result = 1, 0, 0
        
        for j, num in enumerate(nums):
            product *= num
            
            #sliding window
            while product >= target and i < j + 1:
                product /= nums[i]
                i += 1
            result += j - i + 1


        return result

def main():
    sol = Solution()
    print(sol.numSubarrayProductLessThanK([10,5,2,6], k = 100))
    print(sol.numSubarrayProductLessThanK([1,2,3], k = 0))

if __name__ == "__main__": main()
