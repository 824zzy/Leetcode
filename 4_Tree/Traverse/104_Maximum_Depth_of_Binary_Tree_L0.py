# Google
""" Iterative Solution
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        tstack, h = [root], 0
        while tstack:
            next_level = []
            while tstack:
                top = tstack.pop()
                if top.left:
                    next_level.append(top.left)
                if top.right:
                    next_level.append(top.right)
            tstack = next_level
            h += 1
        return h

""" Recursive Solution
"""
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(node, d):
            if not node:
                return d
            return max(dfs(node.left, d+1), dfs(node.right, d+1))
        return dfs(root, 0)