"""
node.right = dfs(node.right, tmp.val) // Call the recursive function in the right subtree to delete the node with the smallest value
"""
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def dfs(node, k):
            if not node: return None
            if node.val==k:
                if not node.left or not node.right:
                    return node.left if node.left else node.right
                else:
                    tmp = node.right
                    while tmp.left: tmp = tmp.left
                    node.val = tmp.val
                    node.right = dfs(node.right, tmp.val)
            elif node.val>k:
                node.left = dfs(node.left, k)
            else:
                node.right = dfs(node.right, k)
            return node

        return dfs(root, key)