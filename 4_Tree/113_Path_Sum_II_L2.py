# Amazon
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.ans = []
        def dfs(node, path, target):
            if not node:
                return 
            path.append(node.val)
            remain = target - node.val
            if remain == 0 and not node.left and not node.right:
                self.ans.append(path)
            dfs(node.left, path[:], remain)
            dfs(node.right, path[:], remain)
        dfs(root, [], sum)
        return self.ans