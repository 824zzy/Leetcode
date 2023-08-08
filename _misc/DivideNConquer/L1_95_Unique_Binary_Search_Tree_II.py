""" https://leetcode.com/problems/unique-binary-search-trees-ii/
Divide and conquer along with dfs
"""
from header import *

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dc(A):
            if not A:
                return [None]
            ans = []
            for i, x in enumerate(A):
                for l in dc(A[:i]):
                    for r in dc(A[i+1:]):
                        node = TreeNode(x)
                        node.left = l
                        node.right = r
                        ans.append(node)
            return ans
        return dc(list(range(1, n+1)))
    
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @cache
        def dfs(l, r):
            if l==r: return [None]
            ans = []
            for i in range(l, r):
                for ll in dfs(l, i):
                    for rr in dfs(i+1, r):
                        ans.append(TreeNode(i, ll, rr))
            return ans
        
        if n: return dfs(1, n+1)
        else: return []