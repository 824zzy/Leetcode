""" https://leetcode.com/problems/two-sum-bsts/
1. DFS search on two trees with cache
"""
from header import *

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        @cache
        def dfs(node1, node2):
            if not node1 or not node2:
                return False
            if node1.val+node2.val==target:
                return True
            if node1.val+node2.val<target:
                return dfs(node1.right, node2) or dfs(node1, node2.right)
            else:
                return dfs(node1.left, node2) or dfs(node1, node2.left)
        return dfs(root1, root2)
    

""" BFS + two pointers
1. Get all the values from tree1 and store in a set
2. Use two pointers to find the sum in the set
"""
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def dfs(node):
            if not node: return []
            l = dfs(node.left)
            r = dfs(node.right)
            return l+[node.val]+r
        A = dfs(root1)
        B = dfs(root2)
        
        l, r = 0, len(B)-1
        while l<len(A) and r>=0:
            if A[l]+B[r]==target: return True
            elif A[l]+B[r]<target:
                l += 1
            else:
                r -= 1
        return False