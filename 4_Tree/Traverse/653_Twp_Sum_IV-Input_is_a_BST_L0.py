class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.t = set()
        self.k = k
        def dfs(node):
            if not node: return False
            if node.val in self.t: return True
            self.t.add(self.k-node.val)
            l = dfs(node.left)
            r = dfs(node.right)
            return l or r
        return dfs(root)