class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        self.ans = []
        def dfs(node):
            if not node:
                return
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val in to_delete:
                if node.left!=None:
                    self.ans.append(node.left)
                if node.right!=None:
                    self.ans.append(node.right)
                return None
            return node
        if root.val not in to_delete:
            sefl.ans.append(root)
        dfs(root)
        return self.ans