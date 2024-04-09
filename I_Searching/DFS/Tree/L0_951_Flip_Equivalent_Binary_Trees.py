class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False

            if node1.val == node2.val:
                rev_l = dfs(node1.left, node2.right)
                rev_r = dfs(node1.right, node2.left)
                l = dfs(node1.left, node2.left)
                r = dfs(node1.right, node2.right)
                return (l and r) or (rev_l and rev_r)
            else:
                return False

        ans = dfs(root1, root2)
        return ans
