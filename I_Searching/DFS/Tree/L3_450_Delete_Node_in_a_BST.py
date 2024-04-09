""" https://leetcode.com/problems/delete-node-in-a-bst/
node.right = dfs(node.right, tmp.val) // Call the recursive function in the right subtree to delete the node with the smallest value
"""


class Solution:
    def deleteNode(
            self,
            root: Optional[TreeNode],
            key: int) -> Optional[TreeNode]:
        def dfs(node, k):
            if not node:
                return None
            if node.val < k:
                node.right = dfs(node.right, k)
            elif node.val > k:
                node.left = dfs(node.left, k)
            else:
                if not node.left or not node.right:
                    return node.left or node.right
                tmp = node.left
                while tmp.right:
                    tmp = tmp.right
                node.val = tmp.val
                node.left = dfs(node.left, tmp.val)
            return node

        return dfs(root, key)
