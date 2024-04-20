class Solution:
    def increasingTriplet(self, nums) -> bool:
        n = len(nums)
        if n<3: return False

        a,b = nums[0], max(nums)
        for c in nums:
            # 3 cases may occur: we have sorted ab so c can be put in 3 positions abc, acb, cab
            # we need to indentiy and handle each case independently

            #abc desired state
            if c>b: return True #c=c
            # acb
            elif c>a: b = c
            # cab
            else: a=c


        return False




def main():
    sol = Solution()
    print(sol.increasingTriplet([1,2,3,4,5]))
    print(sol.increasingTriplet([5,4,3,2,1]))
    print(sol.increasingTriplet([2,1,5,0,4,6]))

if __name__ == "__main__": main()

