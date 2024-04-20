class Solution:
    def twoSum(self, numbers, target: int):
        for num in numbers:
            left, right = 0, len(numbers) - 1

            while left <= right:
                mid = (left + right) // 2
                if num + numbers[mid] == target and numbers.index(num) != mid:
                    return [numbers.index(num) + 1, mid + 1]

                elif num + numbers[mid] <= target: left = mid + 1
                else: right = mid - 1
        return [-1, -1]

def main():
    sol = Solution()
    print(sol.twoSum([2,7,11,15], target = 9))
    print(sol.twoSum([2,3,4], target = 6))
    print(sol.twoSum([-1,0], target = -1))

if __name__ == "__main__": main()