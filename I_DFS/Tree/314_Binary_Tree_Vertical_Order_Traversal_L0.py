""" https://leetcode.com/problems/binary-tree-vertical-order-traversal/
lots of edge cases, carefully sort the tree by vertical order and depth!
"""
from header import *

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = defaultdict(list)
        
        def dfs(node, vert, d):
            if not node: return
            ans[vert].append((d, node.val))
            dfs(node.left, vert-1, d+1)
            dfs(node.right, vert+1, d+1)
            
        dfs(root, 0, 0)
        return [[x[1] for x in sorted(v, key=lambda x: x[0])] for k, v in sorted(ans.items(), key=lambda x: x[0])]
    
"""
[3,9,20,null,null,15,7]
[3,9,8,4,0,1,7]
[3,9,8,4,0,1,7,null,null,null,2,5]
[1,null,3,2,5,null,null,4]
[1,2,3,4,5,6,null,null,7,8,null,null,9,null,10,null,11,10]
"""