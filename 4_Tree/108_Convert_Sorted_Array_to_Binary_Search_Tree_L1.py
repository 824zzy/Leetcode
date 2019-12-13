""" Google and Apple
"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def dfs(l, r):
            if l>r:
                return
            m = (l+r)//2
            node = TreeNode(nums[m])
            node.left = dfs(l, m-1)
            node.right = dfs(m+1, r)
            return node

        ans = dfs(0, len(nums)-1)
        return ans