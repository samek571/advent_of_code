from bisect import bisect_left, bisect_right

class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        n = len(flowers) ; flowers.sort()
        
        #prefixsum
        prefix = [0] * n ; prefix[0] = flowers[0]
        for i in range(1, n):
            prefix[i] = prefix[i-1] + flowers[i]
        #prefix = [flowers[0]] + list(accumulate(flowers))


        #doing greedy and binary search to find for one scenario the best counterpart faster than in On^2
        max_beauty = 0
        for i in range(n, -1, -1):
            if i < n:
                req_for_full = max(0, target - flowers[i])
                
                if req_for_full > newFlowers:
                    break
                
                newFlowers -= req_for_full
                flowers.pop()

            curr_beauty_full = (n - i) * full
            case_beauty = 0


            #binary search
            left, right = 0, target - 1
            while left <= right:
                mid = (left + right) // 2
                idx = bisect_right(flowers, mid)
                
                if idx == 0:
                    left = mid + 1
                else:
                    actual_flowers = prefix[idx - 1]
                    min_flowers = idx * mid
                    extra_flowers = min_flowers - actual_flowers
                    
                    if extra_flowers <= newFlowers:
                        case_beauty = mid * partial
                        left = mid + 1
                    else:
                        right = mid - 1
            
            max_beauty = max(max_beauty, case_beauty + curr_beauty_full)
        
        return max_beauty
