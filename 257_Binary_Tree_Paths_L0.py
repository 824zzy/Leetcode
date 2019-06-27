""" Naive Recursive Tree
"""
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.ans = []

        def findPath(node: TreeNode, path: str) -> None:
            if not node:
                return
            
            path += "->" + str(node.val)
            