class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(o, c, t):
            if not o and not c: return
            if o==t: return c
            l = dfs(o.left, c.left, t)
            r = dfs(o.right, c.right, t)
            if l: return l
            if r: return r
        return dfs(original, cloned, target)