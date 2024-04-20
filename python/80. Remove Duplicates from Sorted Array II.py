class Solution:
    def removeDuplicates(self, nums) -> int:

        start, end, original_lenght, popped = 0, 2, len(nums), 0
        if original_lenght < 2: return original_lenght


        while end <= len(nums)-1:
            if nums[start] == nums[end]:
                nums.pop(end)
                popped+=1

            else:
                start+=1
                end+=1

        return original_lenght-popped





def main():
    sol = Solution()
    print(sol.removeDuplicates([1,2,2,2]))
    print(sol.removeDuplicates([1,2,2,2,3]))
    print(sol.removeDuplicates([1,2,2,2,3,3,3]))
    print(sol.removeDuplicates([1,1,1,2,2,3]))
    print(sol.removeDuplicates([0,0,1,1,1,1,2,3,3]))
    print(sol.removeDuplicates([0,0]))

if __name__ == "__main__": main()

