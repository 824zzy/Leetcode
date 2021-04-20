# Trivial recursive solution
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.ans = []
        
        def dfs(node):
            if not node: return
            self.ans.append(node.val)
            for c in node.children:
                dfs(c)
        
        dfs(root)
        return self.ans

# Smarter iterative solution
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        Q = [root]
        ans = []
        while Q:
            for _ in range(len(Q)):
                cur = Q.pop(0)
                ans.append(cur.val)
                Q = cur.children + Q
        return ans