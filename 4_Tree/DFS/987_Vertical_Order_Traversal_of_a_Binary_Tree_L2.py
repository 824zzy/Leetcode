# Special trick: set a defaultdict function as key for defaultdict

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def x(): return defaultdict(list)
        T = defaultdict(x)
        
        def dfs(node, x, y):
            if not node: return
            T[x][y].append(node.val)
            dfs(node.left, x-1, y+1)
            dfs(node.right, x+1, y+1)
        
        dfs(root, 0, 0)
        vals = [[T[x][y] for y in sorted(T[x])] for x in sorted(T)]
        ans = []
        for l in vals:
            tmp = []
            for i in l: tmp += sorted(i)
            ans.append(tmp)
        return ans