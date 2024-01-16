""" https://leetcode.com/problems/binary-ans-right-side-view/
level order traversal using dfs

Time complexity: O(n)
"""
from header import *

# Only save right most node into ans. Space complexity: O(1)
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def dfs(node, l):
            if not node: return
            if l>len(ans): ans.append(node.val)
            dfs(node.right, l+1)
            dfs(node.left, l+1)
        
        dfs(root, 1)
        return ans

# Record every level of nodes in ans. Space complexity: O(n)
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        ans = defaultdict(list)
        
        def dfs(node, d):
            if not node: return
            ans[d].append(node)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        
        dfs(root, 0)
        return [v[-1].val for k, v in ans.items()]
