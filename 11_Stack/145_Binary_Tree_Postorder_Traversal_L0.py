# Baidu
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
        S, ans = [root], []
        while S:
            currN = S.pop()
            ans.append(currN.val)
            if currN.left:
                S.append(currN.left)
            if currN.right:
                S.append(currN.right)
        return ans[::-1]