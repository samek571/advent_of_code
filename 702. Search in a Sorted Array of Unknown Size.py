# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

'''
we expand the lenght of our subarray by *2, starting at lenght 1 and index 0; goes as follow
0 1
1 2
2 4
...
2^n-1 and 2^n
We dont have to go from 0 since we would have hit this target sooner than at 2^n
(sort of reverse induction or some shit)


Eventually we hit 2 cases;
1. is that the right pointer is bigger than the target --> we perform binary search
in which l = 2^n-1 and r=2^n and easy does it.

2. the harder one is that we just slipped by it (its 17th for example) and the lenght 
of arr is less than 2^(n+1) i.e 29 - we cant extend lenght by *2
--> probably the best would be to do it kinda in reverse --> find the right one by doing some forcycle in which we try to expand rpointer by 2^n-1 and if not then 2^n-2 etc.. we know 2^k+2^k = 2^k+1 therefore its not possible to expand by the same lenght twice in a row. Eventually we reach the target if its within boundaries

time complexity is O(2*logn), once expanding once shrinking
'''


'''hack with the known arr size, we can do pure bs because the api handles exception'''
class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        
        l, r = 0, 10000
        while l <= r:
            mid = (l+r)//2
            val = reader.get(mid)
            
            if val == target: return mid
            elif val < target: l = mid+1
            else: r = mid-1 
        
        return -1


