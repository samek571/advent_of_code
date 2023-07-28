# Definition for a Node.
import collections


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None

        coped = {1: Node(node.val)} ; queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            new = coped[node.val]

            for n in node.neighbors:
                if n.val not in coped:
                    coped[n.val] = Node(n.val)
                    queue.append(n)

                new.neighbors.append(coped[n.val])

        return coped[1]