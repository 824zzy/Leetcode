""" https://leetcode.com/problems/average-of-levels-in-binary-tree/
level order traversal by bfs
"""
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        Q = [root]
        while Q:
            nextQ = []
            sm = 0
            for node in Q:
                sm += node.val
                if node.left: nextQ.append(node.left)
                if node.right: nextQ.append(node.right)
            ans.append(sm/len(Q))
            Q = nextQ
        return ans
                