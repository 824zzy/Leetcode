""" tricky to hundle the node without right child
"""
class Solution:
    def tree2str(self, node: TreeNode) -> str:
        if not node:
            return ""
        if not node.left and not node.right:
            return str(node.val)
        
        if not node.right:
            return str(node.val)+"("+self.tree2str(node.left)+")"
            
        return str(node.val)+"("+self.tree2str(node.left)+")("+self.tree2str(node.right)+")"