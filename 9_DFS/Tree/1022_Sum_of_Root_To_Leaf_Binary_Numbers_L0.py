class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.ans = 0
        
        def dfs(node, path):
            if not node.left and not node.right:
                path += str(node.val)
                self.ans += int(''.join(path), 2)
                return
            
            if node.left:
                dfs(node.left, path+[str(node.val)])
            if node.right:
                dfs(node.right, path+[str(node.val)])
        
        dfs(root, [])
        return self.ans