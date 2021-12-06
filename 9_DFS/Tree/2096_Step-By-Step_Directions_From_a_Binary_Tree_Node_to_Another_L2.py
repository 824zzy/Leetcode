""" https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
solution from ye15: https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/discuss/1612179/Python3-lca
"""
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def lca(node): 
            """Return lowest common ancestor of start and dest nodes."""
            if not node or node.val in (startValue , destValue): return node 
            left, right = lca(node.left), lca(node.right)
            return node if left and right else left or right
        
        root = lca(root) # only this sub-tree matters
        
        def fn(val): 
            """Return path from root to node with val."""
            stack = [(root, "")]
            while stack: 
                node, path = stack.pop()
                if node.val == val: return path 
                if node.left: stack.append((node.left, path + "L"))
                if node.right: stack.append((node.right, path + "R"))
        
        path0 = fn(startValue)
        path1 = fn(destValue)
        return "U"*len(path0) + path1