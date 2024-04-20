from bisect import bisect_left

class Solution:
    '''iterate from back and keep an external sorted list in which nums[i] is going to be added in lgn time, doing this for the whole lenght of nums it makes n*lgn. Looking at the position of inserted number is quite straightworfard'''
    def countSmaller(self, nums: List[int]) -> List[int]:

        sorted_list = []
        counts = []
        
        for num in reversed(nums):
            index = bisect_left(sorted_list, num)
            counts.append(index)
            sorted_list.insert(index, num)
        
        return counts[::-1]
