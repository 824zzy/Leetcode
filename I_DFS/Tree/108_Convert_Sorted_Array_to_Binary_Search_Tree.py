""" L0: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
build tree by finding midle index numbers
"""
class Solution:
    def sortedArrayToBST(self, A: List[int]) -> Optional[TreeNode]:
        def dfs(node, l, r):
            if l>r: return None
            m = (l+r)//2
            node.val = A[m]
            node.left = dfs(TreeNode(0), l, m-1)
            node.right = dfs(TreeNode(0), m+1, r)
            return node
        
        return dfs(TreeNode(0), 0, len(A)-1)