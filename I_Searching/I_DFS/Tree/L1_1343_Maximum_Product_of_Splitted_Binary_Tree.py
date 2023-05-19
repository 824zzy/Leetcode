class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        sums = []
        def dfs(node):
            if not node:
                return 0
            currSum = dfs(node.left)+node.val+dfs(node.right)
            sums.append(currSum)
            return currSum
        
        total = dfs(root)
        return max([(total-x)*x for x in sums]) % (10**9+7)