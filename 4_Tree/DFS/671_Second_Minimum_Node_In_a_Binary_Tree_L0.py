# iterate all values
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.l = set()
        def dfs(node):
            if not node: return
            dfs(node.left)
            dfs(node.right)
            self.l.add(node.val)
        dfs(root)
        return sorted(self.l)[1] if len(self.l)>1 else -1

# stop when meet different values than root
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.m = root.val
        def dfs(node):
            if not node: return float('inf')
            if node.val!=self.m: return node.val
            l = dfs(node.left)
            r = dfs(node.right)
            return min(l, r)
        ans = dfs(root) 
        return ans if ans!=float('inf') else -1