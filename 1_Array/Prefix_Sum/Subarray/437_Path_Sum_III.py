""" L1: https://leetcode.com/problems/path-sum-iii/
prefix sum + back tracking
use prefix sum to find target subarray through back tracking
"""
class Solution:
    def pathSum(self, root: Optional[TreeNode], t: int) -> int:
        cnt = Counter()
        cnt[0] = 1
        self.ans = 0
        
        def dfs(node, prefix):
            if not node: return 0
            prefix += node.val
            self.ans += cnt[prefix-t]
            cnt[prefix] += 1
            dfs(node.left, prefix)
            dfs(node.right, prefix)
            cnt[prefix] -= 1
        
        dfs(root, 0)
        return self.ans