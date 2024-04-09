""" https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/
1. one pass dfs to get nodes
2. another pass to assign the values

TODO: add bfs solution
"""
from header import *


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        mp = defaultdict(list)

        def dfs(node, d):
            if not node:
                return
            mp[d].append(node.val)
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)

        dfs(root, 0)

        def dfs(node, d):
            if not node:
                return
            if d & 1:
                node.val = mp[d].pop()
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)

        dfs(root, 0)
        return root


"""
[2,3,5,8,13,21,34]
[7,13,11]
[0,1,2,0,0,0,0,1,1,1,1,2,2,2,2]
"""
