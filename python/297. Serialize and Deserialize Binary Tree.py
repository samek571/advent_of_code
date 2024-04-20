# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    '''simple bfs'''
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        arr, q=[], []
        if root: q.append(root)

        for node in q:
            if node:
                arr.append(str(node.val))
                q+= node.left, node.right
            else:
                arr.append(str('null'))

        return ",".join(arr)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        q, i, nodes= collections.deque(), 1, data.split(",")
        root = TreeNode(int(nodes[0]))
        q.append(root)

        while q:
            node = q.popleft()

            if nodes[i] != "null":
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            i+=1

            if nodes[i] != 'null':
                node.right = TreeNode(int(nodes[i]))
                q.append(node.right)
            i+=1

        return root




# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize([1, 2]))
# print(ans)