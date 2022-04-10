""" https://leetcode.com/problems/average-of-levels-in-binary-tree/
level order traversal by dfs and defaultdict
"""
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        mp = defaultdict(list)
        
        def dfs(node, d):
            if not node: return
            mp[d].append(node.val)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        
        dfs(root, 0)
        return [sum(v)/len(v) for _, v in mp.items()]