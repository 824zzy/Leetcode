""" Combination of maxDepth and binaryTraverse
"""
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def getHeight(node):
            if not node:
                return 0
            return 1+max(getHeight(node.left), getHeight(node.right))
        h = getHeight(root)
        w = 2**h-1
        ans = [["" for _ in range(w)] for _ in range(h)]
        def dfs(node, dep, l, r):
            if not node:
                return
            m = (l+r)//2
            ans[dep][m] = str(node.val)
            dfs(node.left, dep+1, l, m-1)
            dfs(node.right, dep+1, m+1, r)
        dfs(root, 0, 0, w)
        return ans