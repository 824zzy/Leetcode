class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(node, val, p, d, info):
            if not node:
                return 
            if node.val==val:
                info.append([d, p])
            dfs(node.left, val, node.val, d+1, info)
            dfs(node.right, val, node.val, d+1, info)
            return info
        infox = dfs(root, x, None, 0, [])
        infoy = dfs(root, y, None, 0, [])
        # print(infox, infoy)
        for x, y in zip(infox, infoy):
            if x[0]==y[0] and x[1]!=y[1]:
                return True
        return False