class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        self.ans = 1
        def dfs(node, d):
            if not node:
                return d
            for n in node.children:
                dep = dfs(n, d+1)
                self.ans = max(self.ans, dep)
            return d
        
        dfs(root, 1)
        return self.ans