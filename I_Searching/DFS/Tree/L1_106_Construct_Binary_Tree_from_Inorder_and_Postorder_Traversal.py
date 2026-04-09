""" https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
Build a {val -> inorder_index} map, then recurse on inorder index ranges.
postorder.pop() yields root, so we see root -> right subtree -> left subtree
in reverse. That means we must build the RIGHT child before the LEFT child.
O(n) time, O(n) space.
"""


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pos = {v: i for i, v in enumerate(inorder)}

        def build(lo, hi):
            if lo > hi:
                return None
            v = postorder.pop()
            node = TreeNode(v)
            mid = pos[v]
            node.right = build(mid + 1, hi)   # right first: postorder pops root, then right subtree
            node.left = build(lo, mid - 1)
            return node

        return build(0, len(inorder) - 1)
