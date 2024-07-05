# space saving, better to use if not change t1
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        def dfs(t1, t2):
            if not t1:
                return t2
            if not t2:
                return t1
            t1.val += t2.val
            t1.left = dfs(t1.left, t2.left)
            t1.right = dfs(t1.right, t2.right)
            return t1

        t1 = dfs(t1, t2)
        return t1
