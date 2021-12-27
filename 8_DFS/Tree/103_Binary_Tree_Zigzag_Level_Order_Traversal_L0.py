class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        self.t = collections.defaultdict(list)
        def dfs(node, d):
            if not node: return
            self.t[d].append(node.val)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        dfs(root, 0)
        return [v if i%2==0 else v[::-1] for i, v in enumerate(self.t.values())]