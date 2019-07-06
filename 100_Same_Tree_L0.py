""" Easy recursive solution
"""
# best solution on 2019.6.10
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p or not q:
            return p == q
        elif p.val != q.val:
            return False 
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# solution on 2019.7.4
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)