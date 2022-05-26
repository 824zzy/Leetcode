""" https://leetcode.com/problems/path-sum-ii/
dfs with path or backtracking
"""
class Solution:
    def pathSum(self, root: TreeNode, t: int) -> List[List[int]]:
        self.ans = []

        def dfs(node, path, rm):
            if not node: return 
            path.append(node.val)
            if rm-node.val == 0 and not node.left and not node.right: self.ans.append(path)
            dfs(node.left, path[:], rm-node.val)
            dfs(node.right, path[:], rm-node.val)

        dfs(root, [], t)
        return self.ans


class Solution:
    def pathSum(self, root: Optional[TreeNode], t: int) -> List[List[int]]:
        self.ans = []
        self.stk = []
        
        def dfs(node, sm):
            if not node: return
            self.stk.append(node.val)
            if sm+node.val==t and not node.left and not node.right:
                self.ans.append(self.stk.copy())
            else:
                dfs(node.left, sm+node.val)
                dfs(node.right, sm+node.val)
            self.stk.pop()
            
        dfs(root, 0)
        return self.ans