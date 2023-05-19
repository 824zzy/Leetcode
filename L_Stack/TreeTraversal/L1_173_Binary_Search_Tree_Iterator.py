""" https://leetcode.com/problems/binary-search-tree-iterator/
minor modification on the stack inorder traversal template
"""
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stk = []
        self.node = root

    def next(self) -> int:
        while self.node:
            self.stk.append(self.node)
            self.node = self.node.left
        else:
            ans = self.stk.pop()
            self.node = ans.right
            return ans.val

    def hasNext(self) -> bool:
        return self.stk or self.node