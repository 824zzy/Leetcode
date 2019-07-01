""" Combination of maxDepth and binaryTraverse
"""
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def getHeight(node: TreeNode) -> int:
            if not node:
                return 0
            return 1+max(getHeight(node.left), getHeight(node.right))
        
        h = getHeight(root)
        l = 2**h - 1
        self.ans = [["" for _ in range(l)] for _ in range(h)]

        def dfs(node: TreeNode, l: int, r: int, dep: int):
            if l > r:
                return
            m = (l+r) // 2
            self.ans[dep][m] = str(node.val)
            
            if node.left:
                dfs(node.left, l, m-1, dep+1)
            if node.right:
                dfs(node.right, m+1, r, dep+1)
        dfs(root, 0, l-1, 0)
        return self.ans