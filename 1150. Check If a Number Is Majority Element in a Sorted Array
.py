class Solution:
    #tricky one --> its O(logn)
    def isMajorityElement(self, arr: List[int], target: int) -> bool:
        
        # left_index = bisect_left(arr, target)
        # right_index = bisect_right(arr, target)


        # return right_index-left_index > len(arr)/2





        #just compressed
        return (lambda li, ri: (ri - li) > len(arr) // 2)(bisect_left(arr, target), bisect_right(arr, target))
