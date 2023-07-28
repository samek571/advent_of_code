# Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return


        queue = collections.deque([root])
        while queue:
            size = len(queue)

            for i in range(size):
                node = queue.popleft()
                
                #changing pointer for each node till we can
                if i < size-1:
                    node.next = queue[0] 

                #both children present    
                if node.left:
                    queue.append(node.left) 
                    queue.append(node.right)           
                
                
        return root
