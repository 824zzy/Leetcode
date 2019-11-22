class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        curr = root
        stk, ans = [], []
        while stk or curr:
            while curr:
                stk.append(curr)
                curr = curr.left
            curr = stk.pop()
            ans.append(curr.val)
            curr = curr.right            
        return ans

# BTW Recursive
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.ans = []
        def dfs(node):
            if not node:
                return
            l = dfs(node.left)
            if l:
                self.ans.append(l.val)
            self.ans.append(node.val)
            r = dfs(node.right)
            if r:
                self.ans.append(r.val)
            
        dfs(root)
        return self.ans