class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        paths = []
        self.findPath(root, sum, paths, [])
        return paths

    def findPath(self, node: TreeNode, sum: int, path: List[List[int]], curr: List[int]) -> List[List[int]]:
        if not node:
            return
        
        curr.append(node.val)

        if not node.left and not node.right and sum==node.val:
            path.append(curr[:])
            return
        
        self.findPath(node.left, sum-node.val, path, curr[:])
        self.findPath(node.right, sum-node.val, path, curr[:])
            