class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        nums = set()
        def dfs(node):
            if not node:
                return
            nums.add(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return sorted(list(nums))[1] if len(nums)!=1 else -1