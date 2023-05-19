""" https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
use dict of a dict to store the tree in vertical and depth order
"""
from header import *

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        D = defaultdict(lambda: defaultdict(list))
        
        def dfs(node, v, d):
            if not node: return
            D[v][d].append(node.val)
            dfs(node.left, v-1, d+1)
            dfs(node.right, v+1, d+1)
            
        dfs(root, 0, 0)
        ans = []
        for _, x in sorted(D.items()):
            tmp = []
            for _, v in sorted(x.items(), key=lambda x: x[0]):
                tmp.extend(sorted(v))
            ans.append(tmp)
        return ans