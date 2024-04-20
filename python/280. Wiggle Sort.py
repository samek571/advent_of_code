class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #first thought
        #sort and make nums[i] + nums[n-1-i] as adjecent pairs
        # its (nlogn) + there would be a lot of element shifting by moving the last to bisect one


        # we dont need to sort it, in fact each odd position has to be bigger than even
        # therefore we implement bubblesort for 2 adjecent pairs
        for i in range(len(nums)):
            nums[i:i+2] = sorted(nums[i:i+2], reverse=i%2)

        return nums

def main():
    sol = Solution()
    print(sol.wiggleSort([3,5,2,1,6,4]))
    print(sol.wiggleSort([6,6,5,6,3,8]))

if __name__ == "__main__": main()