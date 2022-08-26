""" https://leetcode.com/problems/find-leaves-of-binary-tree/
use post order traversal to find the leaves of the tree along with a defaultdict 
whose key is the depth of the node and value is the list of leaves at that depth

Time complexity: O(n)
Space complexity: O(n)
"""
from header import *

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            d = max(l, r)
            ans[d].append(node.val)
            return d+1
        
        dfs(root)
        return list(ans.values())