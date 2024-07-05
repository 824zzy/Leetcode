class Solution:
    def maxDepth(self, root: "Node") -> int:
        self.ans = 0

        def dfs(node, d):
            if not node:
                return
            self.ans = max(self.ans, d)
            for n in node.children:
                dfs(n, d + 1)

        dfs(root, 1)
        return self.ans
