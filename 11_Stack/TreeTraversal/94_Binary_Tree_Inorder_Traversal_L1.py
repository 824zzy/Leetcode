""" https://leetcode.com/problems/binary-tree-inorder-traversal/
algorithm template
"""
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk = []
        ans = []
        node = root
        while stk or node:
            if node:
                stk.append(node)
                node = node.left
            else:
                node = stk.pop()
                ans.append(node.val)
                node = node.right
        return ans