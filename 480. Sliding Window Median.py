import heapq

class Solution:
    def medianSlidingWindow(self, numbers, k: int):# -> List[float]:
        result = []
        window = []
        heapq.heapify(window)
        for i, n in enumerate(numbers):
            if i >= k:
                if k % 2 == 0:
                    result.append(0.5 * (window[k//2-1] + window[k//2]))
                else:
                    result.append(window[k//2])

                window.remove(numbers[i-k])
                heapq.heapify(window)
            heapq.heappush(window, n)
            window.sort() # somehow has to be fucking fixed cuz this sort of one improper element is O(n)
            #  instead of the logn


        if k % 2 == 0: result.append(0.5 * (window[k//2-1] + window[k//2]))
        else: result.append(window[k//2])


        return result


def main():
    sol = Solution()
    print(sol.medianSlidingWindow([1,3,-1,-3,5,3,6,7], k = 3)) #[1, -1, -1, 3, 5, 6]
    print(sol.medianSlidingWindow([1,2,3,4,2,3,1,4,2], k = 3)) #[2, 3, 3, 3, 2, 3, 2]

if __name__ == "__main__": main()