class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        def dfs(node, parent, d):
            if not node:
                new = TreeNode(val)
                if d=='l':
                    parent.left = new
                elif d=='r':
                    parent.right = new
                return
            if node.val<val:
                dfs(node.right, node, 'r')
            else:
                dfs(node.left, node, 'l')
                
        dfs(root, None, None)
        return root
    
# Smarter solution
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
			
        return root