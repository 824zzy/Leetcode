""" https://leetcode.com/problems/height-of-binary-tree-after-subtree-removal-queries/
1. DFS to find two hash tables: node as key, depth as value, and depth as key, node as value
2. compute the third hash table for finding the most deepest two nodes of each depth
3. for each query, there are two cases:
    1. if the node has no cousin, then the answer is the depth of the node minus 1
    2. if the node has a cousin, then the answer is the depth of the node or the most deepest node of the cousin's depth
"""
from header import *

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        node2d = {}
        d2node = defaultdict(set)
        
        def dfs(node, d):
            if not node: return 0
            d2node[d].add(node.val)
            l = dfs(node.left, d+1)
            r = dfs(node.right, d+1)
            v = max(l, r)
            node2d[node.val] = (d, max(l, r))
            return v+1
        
        dfs(root, 0)
        
        mp = defaultdict(list)
        for d, n in d2node.items():
            vals = []
            for nn in n:
                vals.append((node2d[nn][0]+node2d[nn][1], nn))
            vals.sort(reverse=True)
            mp[d] = vals
        
        ans = []
        for q in queries:
            if len(d2node[node2d[q][0]])>1:
                d = node2d[q][0]
                if q!=mp[d][0][1]:
                    ans.append(mp[d][0][0])
                else:
                    ans.append(mp[d][1][0])
            else:
                ans.append(node2d[q][0]-1)
        return ans
                    
            
""" [2] [3,2,3,2] [1,0,3,3,3]
[1,3,4,2,null,6,5,null,null,null,null,null,7]
[4]
[5,8,9,2,1,3,7,4,6]
[3,2,4,8]
[1,null,5,3,null,2,4]
[3,5,4,2,4]
"""