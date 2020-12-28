# Same idea of 865
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node: return 0, None
            l, r = dfs(node.left), dfs(node.right)
            if l[0]>r[0]: return l[0]+1, l[1]
            elif l[0]<r[0]: return r[0]+1, r[1]
            else: return l[0]+1, node
        return dfs(root)[1]