class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        #k must be in nums because we consider either mid element or mid-1, no average as usually.
        # there fore it is say to assume

        result = 0
        n = len(nums)
        k_idx = nums.index(k)
        balancing_other_side_hashmap = collections.defaultdict(int)


        #now we can count how many elements are greater and less than the k after k_index
        val = 0
        for idx in range(k_idx,n):
            if nums[idx] > k: val +=1
            elif nums[idx]<k: val -=1
            #else no harm done

            balancing_other_side_hashmap[val]+=1

        #now we do the same from k_idx to 0 just in reverse order, in the end we travel the whole array once so its O(n)
        val = 0
        for idx in range(k_idx,-1,-1):
            if nums[idx] > k: val +=1
            elif nums[idx]<k: val -=1
            #else no harm done

            #since in even lenght we are taking the mid closer to the left, its safe to assume that for any lenght of satisfying array, we get 2 results because in this case odd is a subset of even.
            result += balancing_other_side_hashmap[-val]
            result += balancing_other_side_hashmap[-val+1]

        return result
