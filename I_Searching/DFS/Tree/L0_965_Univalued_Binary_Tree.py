# bool solution
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        if root.left and root.left.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)


# traverse solution


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.val = []

        def dfs(node: TreeNode):
            if not node:
                return

            self.val.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return len(set(self.val)) == 1


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.v = root.val
        self.ans = True

        def dfs(node):
            if not node:
                return
            if node.val != self.v:
                self.ans = False
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.ans
