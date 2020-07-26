class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        tree = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            tree.append(node.val)
            dfs(node.right)
        dfs(root)
        
        lenth = len(tree)
        def create(nodes, i):
            if i==lenth:
                return
            curr = TreeNode(nodes[i])
            curr.right = create(nodes, i+1)
            return curr
        
        ans = create(tree, 0)
        return ans