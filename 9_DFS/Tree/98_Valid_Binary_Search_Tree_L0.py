# Facebook
class Solution:
    def isValidBST(self, node: TreeNode, l=-float('inf'), r=float('inf')) -> bool:

        if not node: return True
        if l>=node.val or r<=node.val: return False
        left = self.isValidBST(node.left, l, node.val)
        right = self.isValidBST(node.right, node.val, r)
        return left and right
    
    
class Solution:
    def isValidBST(self, node: TreeNode, l=-float('inf'), r=float('inf')) -> bool:
        self.val = []
        
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            self.val.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return all(self.val[i] < self.val[i+1] for i in range(len(self.val)-1))