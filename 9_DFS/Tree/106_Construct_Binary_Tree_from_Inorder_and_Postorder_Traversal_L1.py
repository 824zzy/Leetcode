""" https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""
class Solution:
    def buildTree(self, I: List[int], P: List[int]) -> Optional[TreeNode]:
        def dfs(I, P):
            if not I and not P: return None
            v = P.pop()
            node = TreeNode(v)
            idx = I.index(v)
            node.left = dfs(I[:idx], P[:idx])
            node.right = dfs(I[idx+1:], P[idx:])
            return node
        return dfs(I, P)