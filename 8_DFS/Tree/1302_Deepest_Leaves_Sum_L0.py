class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        L = defaultdict(list)
        
        def dfs(node, d):
            if not node: return
            if not node.left and not node.right:
                L[d].append(node.val)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
            
        dfs(root, 0)
        maxL = sorted(L.items(), key=lambda x: x[0])
        return sum(maxL[-1][-1])