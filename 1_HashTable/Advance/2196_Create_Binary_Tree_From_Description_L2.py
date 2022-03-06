""" https://leetcode.com/problems/create-binary-tree-from-descriptions/
construct tree by hash table and use seen set to find root
"""
class Solution:
    def createBinaryTree(self, A: List[List[int]]) -> Optional[TreeNode]:
        mp = {}
        seen = set()
        for p, c, left in A: 
            if p not in mp: mp[p] = TreeNode(p)
            if c not in mp: mp[c] = TreeNode(c)
            if left: mp[p].left = mp[c]
            else: mp[p].right = mp[c]
            seen.add(c)
        for p, _, _ in A: 
            if p not in seen: return mp[p]