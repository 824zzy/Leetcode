class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node, p):
            if not node: return
            if not node.left and not node.right:
                p += [node.val]
                cntp = collections.Counter(p)
                self.ans += sum([v%2 for v in cntp.values()])<2
                return 
            dfs(node.left, p+[node.val])
            dfs(node.right, p+[node.val])
        dfs(root, [])
        return self.ans