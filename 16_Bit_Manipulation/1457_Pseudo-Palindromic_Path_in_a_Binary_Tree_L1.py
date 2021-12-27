class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node, mask):
            if not node: return
            mask ^= (1<<node.val-1)
            if not node.left and not node.right:
                self.ans += mask==0 or math.log(mask, 2)%1==0
            dfs(node.left, mask)
            dfs(node.right, mask)
        dfs(root, 0)
        return self.ansa