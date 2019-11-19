""" Iteration: use For loop to record level nodes
"""
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        ans = []
        while queue:
            curr = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                curr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                ans.append(curr)
        return ans

""" Recursion: use defaultdict to record level nodes
"""
from collections import defaultdict
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = defaultdict(list)
        def dfs(node, d):
            if not node:
                return
            ans[d].append(node.val)
            dfs(node.left, d+1)
            dfs(node.right ,d+1)
        dfs(root, 0)
        return ans.values()