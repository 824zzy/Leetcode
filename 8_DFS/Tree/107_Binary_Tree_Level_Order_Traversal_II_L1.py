""" https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)
        
        def dfs(node, d):
            if not node: return
            ans[d].append(node.val)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        
        dfs(root, 0)
        return [v for k, v in sorted(ans.items(), key=lambda x: (-x[0]))]