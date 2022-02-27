""" https://leetcode.com/problems/maximum-width-of-binary-tree/
if we label the node of each level nodes by column from 0 to n, then we have:
node.left.column = node.column*2
node.right.column = node.column*2+1
"""
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        Q = [(root, 0)]
        ans = 0
        while Q:
            ans = max(ans, Q[-1][1]-Q[0][1]+1)
            for _ in range(len(Q)):
                node, col = Q.pop(0)
                if node.left: Q.append([node.left, 2*col])
                if node.right: Q.append([node.right, 2*col+1])
        return ans