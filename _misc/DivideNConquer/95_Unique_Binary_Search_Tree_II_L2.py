""" https://leetcode.com/problems/unique-binary-search-trees-ii/
Divide and conquer along with dfs
"""
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