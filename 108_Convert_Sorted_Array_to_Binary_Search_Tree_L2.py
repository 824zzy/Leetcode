""" Google and Apple
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# class Solution:
#     def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
#         def convert(left, right):
#             if left > right:
#                 return None
#             mid = (left+right) // 2
#             node = TreeNode(nums[mid])
#             node.left = convert(left, mid-1)
#             node.right = convert(mid+1, right)
#             return node
            
#         # TODO: resursive method
#         l, r = 0, len(nums)-1
#         m = (l + r) // 2
#         t, root = TreeNode(nums[m])
#         while(l < r):
#             m = (l + r) // 2
            
            
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
        