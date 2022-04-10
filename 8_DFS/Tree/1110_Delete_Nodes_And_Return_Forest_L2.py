""" https://leetcode.com/problems/delete-nodes-and-return-forest/
traverse the tree, add node to ans iff parent value is None
"""
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        
        def dfs(node,  pval):
            if not node: return
            if node.val in to_delete:
                node.left = dfs(node.left, None)
                node.right = dfs(node.right, None)
                return 
            else:
                if not pval: ans.append(node)
                node.left = dfs(node.left, node.val)
                node.right = dfs(node.right, node.val)
                return node
            
        dfs(root, None)
        return ans