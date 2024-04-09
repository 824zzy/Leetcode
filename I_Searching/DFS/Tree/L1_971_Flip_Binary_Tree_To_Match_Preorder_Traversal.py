"""
Global integer i indicates next index in voyage v.
If current node == null, it's fine, we return true
If current node.val != v[i], doesn't match wanted value, return false
If left child exist but don't have wanted value, flip it with right child.
"""


class Solution:
    def flipMatchVoyage(self, root: TreeNode, V: List[int]) -> List[int]:
        self.ans = []
        self.i = 0

        def dfs(node):
            if not node:
                return True
            elif node.val != V[self.i]:
                return False
            elif node.val == V[self.i]:
                self.i += 1
                if node.left and node.left.val != V[self.i]:
                    self.ans.append(node.val)
                    return dfs(node.right) and dfs(node.left)
                else:
                    return dfs(node.left) and dfs(node.right)

        is_match = dfs(root)
        return self.ans if is_match else [-1]
