""" https://leetcode.com/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/description/
level-ordered dfs + cycle sort (https://www.geeksforgeeks.org/cycle-sort/)
"""
from header import *

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def cyclesort(A):
            mp = {x: i for i, x in enumerate(sorted(A))}
            seen = {x: False for x in A}
            ans = 0
            for i, x in enumerate(A):
                cnt = 0
                while i!=mp[x] and not seen[x]:
                    cnt += 1
                    seen[x] = True
                    i = mp[x]
                    x = A[i]
                ans += max(0, cnt-1)
            return ans            
        
        mp = defaultdict(list)
        def dfs(node, d):
            if not node: return
            mp[d].append(node.val)
            dfs(node.left, d+1)
            dfs(node.right, d+1)        
        dfs(root, 0)

        ans = 0
        for k, v in mp.items():
            ans += cyclesort(v)
        return ans