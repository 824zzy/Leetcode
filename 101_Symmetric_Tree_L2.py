class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.symetric(root.left, root.right)
    
    def symetric(self, left: TreeNode, right: TreeNode) -> bool:
        if not left or not right:
            return left == right
        if left.val != right.val:
            return False
        
        return self.symetric(left.left, right.right) and self.symetric(left.right, right.left)