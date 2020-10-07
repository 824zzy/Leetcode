class Solution:
    def searchBST(self, node: TreeNode, val: int) -> TreeNode:
        if not node:
            return None
        elif node.val==val:
            return node
        else:
            if node.val>val:
                ans = self.searchBST(node.left, val)
            else:
                ans = self.searchBST(node.right, val)
        return ans