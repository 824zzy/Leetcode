""" https://leetcode.com/problems/binary-tree-vertical-order-traversal/
lots of edge cases, carefully sort the tree by vertical order and depth!
"""
from header import *

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        T = defaultdict(list)
        
        def dfs(node, p, d):
            if not node:
                return
            T[p].append((d, node.val))
            dfs(node.left, p-1, d+1)
            dfs(node.right, p+1, d+1)
        dfs(root, 0, 0)
        
        ans = []
        for x in sorted(T.items()):
            ans.append(y[1] for y in sorted(x[1], key=lambda x: x[0]))
        return ans
    
"""
[3,9,20,null,null,15,7]
[3,9,8,4,0,1,7]
[3,9,8,4,0,1,7,null,null,null,2,5]
[1,null,3,2,5,null,null,4]
[1,2,3,4,5,6,null,null,7,8,null,null,9,null,10,null,11,10]
"""