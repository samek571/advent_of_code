class Solution:
    '''find the last index of the max element ofc by binary search
    perform 2 binary searches one with 0:idx and second idx+1:len-1
    O(logn) overall'''

    '''there is this "hack" with onepass which could be done in O(n) and since i fucking hate writting code, its indeed the option to go with ajajajja'''
    def search(self, nums: List[int], target: int) -> bool:
        
        # dumb hacker
        # for i in nums:
        #     if i == target: return True
        
        # return False


        # more of a built in the hacker way
        return target in nums
