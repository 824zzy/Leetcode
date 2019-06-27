""" Google and Apple
"""
# Recursice Solution
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def convert(left, right):
            if left > right:
                return None
            mid = (left+right) // 2
            node = TreeNode(nums[mid])
            node.left = convert(left, mid-1)
            node.right = convert(mid+1, right)
            return node
        return convert(0, len(nums)-1)

# Iteration Solution
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        l, r = 0, len(nums)-1
        t, root = TreeNode(nums[m])
        while l < r:
            m = (l + r) // 2
        