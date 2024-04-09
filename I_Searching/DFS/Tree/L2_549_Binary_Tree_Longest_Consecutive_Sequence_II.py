""" https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/
For each node, we keep track of the longest consecutive increasing and decreasing sequence that starts at that node.
"""
from header import *


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        # increase
        def dfs(node):
            if not node:
                return None, None
            li, ld = dfs(node.left)
            ri, rd = dfs(node.right)

            cnti = 1
            cntd = 1
            if node.left and node.left.val + 1 == node.val:
                cnti += ld
                ld += 1
            else:
                ld = 1
            if node.left and node.left.val - 1 == node.val:
                cntd += li
                li += 1
            else:
                li = 1
            if node.right and node.right.val + 1 == node.val:
                cntd += rd
                rd += 1
            else:
                rd = 1
            if node.right and node.right.val - 1 == node.val:
                cnti += ri
                ri += 1
            else:
                ri = 1
            self.ans = max(self.ans, cnti, cntd)
            return max(li, ri), max(ld, rd)

        dfs(root)
        return self.ans


"""
[1,2,3]
[2,1,3]
[1,2,3,4]
[1,2,1]
[2,null,3,4,null,1]
[1,2,null,3,null,4]
[4,2,null,3,1,null,null,5]
[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
"""
