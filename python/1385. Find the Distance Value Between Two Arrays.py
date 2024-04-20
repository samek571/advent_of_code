class Solution:
    def findTheDistanceValue(self, arr1, arr2, target: int) -> int:
        len1, len2 = len(arr1), len(arr2)

        if target == 0: return 0

        arr2, returnment = sorted(arr2), 0

        for i in arr1:
            left, right = 0, len2-1
            valid = True

            while left <= right:
                mid = (left + right) // 2
                if arr2[mid] == i or abs(i- arr2[mid]) <= target:
                    valid=False
                    break

                elif arr2[mid] < i:
                    left = mid + 1
                else:
                    right = mid - 1

            returnment += valid

        return returnment





def main():
    sol = Solution()
    print(sol.findTheDistanceValue([4,5,8], [10,9,1,8], 2))
    print(sol.findTheDistanceValue(arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], target = 3))
    print(sol.findTheDistanceValue(arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], target = 6))

if __name__ == "__main__": main()