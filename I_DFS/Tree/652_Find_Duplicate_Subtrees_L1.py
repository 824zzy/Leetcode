""" https://leetcode.com/problems/find-duplicate-subtrees/
serialization(pre-order dfs)
"""
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        mp = defaultdict(list)
        
        def dfs(node):
            if not node: return '#'
            s = str(node.val)+','+dfs(node.left)+','+dfs(node.right)
            mp[s].append(node)
            return s 
        
        dfs(root)
        return [v[0] for k, v in mp.items() if len(v)>1]