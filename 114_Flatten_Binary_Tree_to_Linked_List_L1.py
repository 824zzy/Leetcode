# Readable dfs
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = None
        def dfs(node: TreeNode) -> None:
            if not node:
                return
            dfs(node.right)
            dfs(node.left)
            
            node.right = self.prev
            node.left = None
            self.prev = node
        
        dfs(root)

# `while` trick can not undertand
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)

        if root.left:
            node = root.left
            while node.right: # Can not understand this part
                node = node.right
            node.right = root.right
            root.right = root.left
            root.left = None



