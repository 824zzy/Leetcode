""" Hash table tree solution: 52ms
"""
from collections import defaultdict
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(node: TreeNode, cur_sum: int) -> None:
            self.count += d[cur_sum-sum]
            d[cur_sum] += 1
            if node.left:
                dfs(node.left, cur_sum+node.left.val)
            if node.right:
                dfs(node.right, cur_sum+node.right.val) 
        
        self.count = 0
        d = defaultdict(int)
        d[0] = 1
        if root:
            dfs(root, root.val)
        return self.count

""" Double Recursion solution: 1052ms
"""
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        def dfs(node: TreeNode, curSum: int) -> int:
            count = 0
            
            if node.val == curSum:
                count += 1
            
            count += dfs(node.left, curSum-node.left.val)
            count += dfs(node.right, curSum-node.right.val)
            return count

        return dfs(root, sum)+self.pathSum(root.left, sum)+self.pathSum(root.right, sum)