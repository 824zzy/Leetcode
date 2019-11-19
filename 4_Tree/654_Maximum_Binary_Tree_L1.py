# Don't use index as dfs parameters!
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def dfs(nums):
            if not nums:
                return None
            pivot = nums.index(max(nums))
            node = TreeNode(nums[pivot])
            node.left = dfs(nums[:pivot])
            node.right = dfs(nums[pivot+1:])
            return node
        
        ans = dfs(nums)
        return ans