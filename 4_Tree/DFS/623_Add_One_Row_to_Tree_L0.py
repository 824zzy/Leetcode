class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d==1:
            new = TreeNode(v)
            new.left = root
            return new
        def dfs(node, dep):
            if not node: return
            if dep==d-1:
                newL = TreeNode(v)
                newL.left = node.left
                node.left = newL
                newR = TreeNode(v)
                newR.right = node.right
                node.right = newR
                return
            dfs(node.left, dep+1)
            dfs(node.right, dep+1)
        dfs(root, 1)
        return root