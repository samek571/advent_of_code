# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #yeah it is important to add this n:n since len+1 refers to nothing
        hsh = {None:None}

        node = head
        while node:
            hsh[node] = Node(node.val)
            node = node.next
        
        node = head
        while node:
            hsh[node].next = hsh[node.next]
            hsh[node].random = hsh[node.random]

            node = node.next
        
        return hsh[head]
