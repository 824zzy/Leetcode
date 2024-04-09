""" https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
pre-order traversal of the tree to serialize and deserialize.
Note that serialization/deserialization is commonly used in other problems
"""
from header import *


class Codec:
    def serialize(self, node):
        if not node:
            return '#'
        return str(node.val) + "," + self.serialize(node.left) + \
            ',' + self.serialize(node.right)

    def deserialize(self, data):
        Q = data.split(',')

        def dfs(Q):
            val = Q.pop(0)
            if val == '#':
                return None
            node = TreeNode(val)
            node.left = dfs(Q)
            node.right = dfs(Q)
            return node

        return dfs(Q)
