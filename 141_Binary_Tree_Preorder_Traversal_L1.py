""" Recursive
"""
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        self.preorder(root, ans)
        return ans
    
    def preorder(self, root: TreeNode, values: List[int]) -> List[int]:
        if not root:
            return
        values.append(root.val)
        self.preorder(root.left, values)
        self.preorder(root.right, values)

""" Iteritive
"""
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans, stack = [], []
        curr = root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                ans.append(curr.val)
                curr = curr.left
            
            curr = stack.pop().right
            
                