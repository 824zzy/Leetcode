""" https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
dfs along with original and cloned tree
"""


class Solution:
    def getTargetCopy(
            self,
            ori: TreeNode,
            cln: TreeNode,
            t: TreeNode) -> TreeNode:
        def dfs(ori, cln):
            if not ori:
                return None
            if ori == t:
                return cln
            l = dfs(ori.left, cln.left)
            r = dfs(ori.right, cln.right)
            return l or r

        return dfs(ori, cln)
