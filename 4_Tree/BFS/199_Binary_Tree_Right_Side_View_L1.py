""" variants of level order traverse
"""
# recursive version
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        tree = collections.defaultdict(list)
        
        def dfs(node, d):
            if not node: return
            tree[d].append(node)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        
        dfs(root, 0)
        return [v[-1].val for k, v in tree.items()]

# iterative version
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