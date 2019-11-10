class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node):
            if not node:
                return
            if (node.val>=p.val and node.val<=q.val) or \
               (node.val<=p.val and node.val>=q.val):
                return node
            l = dfs(node.left)
            r = dfs(node.right)
            return l if l else r
        ans = dfs(root)
        return ans