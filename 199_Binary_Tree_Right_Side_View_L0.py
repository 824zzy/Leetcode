""" Variant of level order traverse
"""
# Recursive version
from collections import defaultdict
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        self.d = defaultdict(list)
        
        def dfs(node: TreeNode, l: int) -> None:
            if not node:
                return
            self.d[l].append(node.val)
            dfs(node.left, l+1)
            dfs(node.right, l+1)
            
        dfs(root, 1)
        return [l[-1] for l in self.d.values()]

# Iterative version
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        queue = [root]
        ans = []
        
        while queue:
            ans.append(queue[-1].val)
            for _ in range(len(queue)):
                cur = queue.pop(0)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return ans