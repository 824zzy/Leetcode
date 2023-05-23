""" https://leetcode.com/problems/delete-nodes-and-return-forest/
traverse the tree, add node to ans iff parent value is None
"""
from header import *

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        
        def dfs(node, parent):
            if not node: return
            if node.val in to_delete:
                dfs(node.left, None)
                dfs(node.right, None)
                return
            else:
                if not parent: ans.append(node)
                node.left = dfs(node.left, node)
                node.right = dfs(node.right, node)
                return node
            
        dfs(root, None)
        return ans