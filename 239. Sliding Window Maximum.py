import heapq

class Solution:
    def maxSlidingWindow(self, nums, k: int):# -> List[int]:

        # little trick to get the largest in sorted list
        window = [(-nums[i], i) for i in range(k-1)]
        heapq.heapify(window)


        # push curr (index, -value)
        # pop smallest by index
        # append "smallest"
        hovno = []
        for i in range(k-1, len(nums)):
            heapq.heappush(window, (-nums[i], i))

            #skimming window only if it is necesarry, O(n) space regardless
            while window[0][1] <= i - k:
                heapq.heappop(window)

            hovno.append(-window[0][0])



        return hovno

def main():
    sol = Solution()
    print(sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,1,0], k = 3))
    print(sol.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
    print(sol.maxSlidingWindow(nums = [1], k = 1))

if __name__ == "__main__": main()