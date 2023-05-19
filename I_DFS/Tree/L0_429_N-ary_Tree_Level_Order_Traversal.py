""" https://leetcode.com/problems/n-ary-tree-level-order-traversal/

"""
from header import *
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        mp = defaultdict(list)
        
        def dfs(node, d):
            if not node: return
            mp[d].append(node.val)
            for c in node.children:
                dfs(c, d+1)
                
        dfs(root, 0)
        return mp.values()