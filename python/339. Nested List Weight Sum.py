# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    """first thought was to make a string out of it and
    1. by regex filter out numbers
    2. each [ makes depth +1 and ] is -1
    so if we would encounter something diff than { ',', ' ', ']', '[' }
    we would know its the number from regex and by the current depth made the multiplication

    con is that its basically O(len(str(list))) instead of O(n) where n is any number (the level doesnt matter)
    """

    def depthSum(self, nestedList) -> int:
        #might be 1d 2d 3d typa matrix or integer
        #if its integer we are done with the element and multiply value by depth
        # if not by iterative recursion we add them to the stack
        # (dfs in this case since its easier to implement, but bfs is more intuitive)
        stck = [(x, 1) for x in nestedList]

        cnt=0
        while stck:
            typa, depth = stck.pop()

            if typa.isInteger():
                cnt+=typa.getInteger()*depth
            else:
                # this is at least 1D matrix
                for ele in typa.getList():
                    stck.append((ele, depth+1))

        return cnt
