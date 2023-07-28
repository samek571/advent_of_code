class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:

        # arr=sorted(zip(nums2,nums1), reverse=True)

        # print(arr)
        # print(arr[k-1][0])
        # print(sum(map(lambda x: x[0], arr[:k])))
        # return arr[k-1][0] * sum(map(lambda x: x[1], arr[:k]))

        pairs = zip(nums1,nums2)
        pairs = sorted(pairs, key=lambda p: p[1], reverse = True)
        minHeap = []
        n1Sum = 0
        res = 0

        for n1, n2 in pairs:
            heapq.heappush(minHeap,n1)

            #only k greatest
            n1Sum+=n1
            if len(minHeap)>k:
                n1Sum -= heapq.heappop(minHeap)

            #obviously marking the best scenario out of the n-k+1 
            if len(minHeap)==k:
                res = max(res,n1Sum*n2)
        
        
        return res
