class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.ans = []

        def dfs(node):
            if not node:
                return
            for n in node.children:
                dfs(n)
            self.ans.append(node.val)
        dfs(root)
        return self.ans
