""" Naive Recursive Tree
"""
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.ans = []
        def dfs(node: TreeNode, curPath: str):
            if not node:
                return
            if not node.left and not node.right:
                curPath += str(node.val)
                self.ans.append(curPath)
                return 
            curPath += str(node.val) + '->'
            dfs(node.left, curPath)
            dfs(node.right, curPath)
        
        dfs(root, '')
        return self.ans
            