""" Recursively
"""
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        def post(root):
            if not root:
                return
            post(root.left)
            post(root.right)
            res.append(root.val)
            return res
        post(root)
        return res

""" Iteratively
"""
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack1 = []
        stack2 = []
        node = root
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node.val)
        
        res = stack2[::-1]
        return res