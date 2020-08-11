class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.tree1 = []
        self.tree2 = []
        def dfs1(node):
            if not node.left and not node.right:
                self.tree1.append(node.val)
                return
            if node.left:
                dfs1(node.left)
            if node.right:
                dfs1(node.right)
        
        def dfs2(node):
            if not node.left and not node.right:
                self.tree2.append(node.val)
                return
            if node.left:
                dfs2(node.left)
            if node.right:
                dfs2(node.right)
        
        dfs1(root1)
        dfs2(root2)
        # print(self.tree1, self.tree2)
        return self.tree1==self.tree2
