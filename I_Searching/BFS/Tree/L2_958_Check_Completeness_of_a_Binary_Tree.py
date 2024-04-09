""" https://leetcode.com/problems/check-completeness-of-a-binary-tree/
use flag to check if there is a missing node
"""
from header import *


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        Q = [root]
        pre_cnt = 0.5
        d = -1
        while Q:
            nxtQ = []
            miss = False
            if pre_cnt != 2**d:
                return False
            pre_cnt = len(Q)
            for node in Q:
                if not node:
                    miss = True
                else:
                    if miss:
                        return False
                    nxtQ.append(node.left)
                    nxtQ.append(node.right)
            Q = nxtQ
            d += 1
        return True
