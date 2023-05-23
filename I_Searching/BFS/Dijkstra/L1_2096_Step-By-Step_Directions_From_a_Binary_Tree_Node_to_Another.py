""" https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
Use dfs to construct a graph and dijkstra to find shortest path
"""
class Solution:
    def getDirections(self, root: Optional[TreeNode], start: int, dest: int) -> str:
        G = defaultdict(dict)
        
        def dfs(node):
            if not node: return
            if node.left:
                G[node.val][node.left.val] = 'L'
                G[node.left.val][node.val] = 'U'
                dfs(node.left)
            if node.right:
                G[node.val][node.right.val] = 'R'
                G[node.right.val][node.val] = 'U'
                dfs(node.right)
        
        dfs(root)
        Q = [(0, start, '')]
        seen = set()
        seen.add(start)
        ans = ''
        while Q:
            s, i, p = heappop(Q)
            if i==dest: return p
            for j in G[i]:
                if j not in seen:
                    heappush(Q, (s+1, j, p+G[i][j]))
                    seen.add(j)
