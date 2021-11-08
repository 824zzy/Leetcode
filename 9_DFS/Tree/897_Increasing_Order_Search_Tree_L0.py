class Solution:
    def increasingBST(self, root: TreeNode, tail=None) -> TreeNode:
        if not root: 
            return tail
        result = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return result
    
    
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


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.ans = TreeNode(0)
        self.prev = None
        self.dummy = self.ans
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.ans.val = node.val
            self.ans.right = TreeNode(0)
            self.prev = self.ans
            self.ans = self.ans.right
            dfs(node.right)
        
        dfs(root)
        self.prev.right = None
        return self.dummy