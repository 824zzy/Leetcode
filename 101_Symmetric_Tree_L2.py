""" A little tricky pythonic style
if not left or not right:
    return left == right

which is equal to:

if not left and not right:
    return True
if not left or not right:
    return False
"""
# Combined recursive
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        def dfs(left: TreeNode, right: TreeNode) -> bool:
            if not left or not right:
                return left == right
            if left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)
        
        return dfs(root.left, root.right)


# Seperate recursive
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