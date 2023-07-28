class Solution:
    #mountain and valley pricipe
    def wiggleMaxLength(self, nums):
        if len(nums) == 1: return 1

        # Remove duplicates
        i = 1
        for j in range(1, len(nums)):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i += 1
        
        n = i # n as lenght
        if n <= 2: return n

        count = 0
        for i in range(1, n-1):
            #uprise or downfall
            if (nums[i]-nums[i-1])*(nums[i+1]-nums[i]) < 0:
                count += 1

        return count + 2 # at least2 elements exist at all cost (unless its a 1element array but thats handled already)


def main():
    sol = Solution()
    print(sol.wiggleMaxLength([3, 3, 3, 2, 5]))
    print(sol.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
    print(sol.wiggleMaxLength([0,0]))
    print(sol.wiggleMaxLength([0,0,0]))

if __name__ == "__main__":
    main()
