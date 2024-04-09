""" https://leetcode.com/problems/construct-quad-tree/
divide the trees by checking if all the values are the same
"""
from header import *


class Solution:
    def construct(self, G: List[List[int]]) -> 'Node':
        def fn(x0, x1, y0, y1):
            vals = {G[i][j] for i, j in product(range(x0, x1), range(y0, y1))}
            if len(vals) == 1:
                return Node(vals.pop(), True, None, None, None, None)
            tl = fn(x0, (x0 + x1) // 2, y0, (y0 + y1) // 2)
            tr = fn(x0, (x0 + x1) // 2, (y0 + y1) // 2, y1)
            bl = fn((x0 + x1) // 2, x1, y0, (y0 + y1) // 2)
            br = fn((x0 + x1) // 2, x1, (y0 + y1) // 2, y1)
            return Node(None, False, tl, tr, bl, br)

        return fn(0, len(G), 0, len(G))


# Definition for a QuadTree node.
class Node:
    def __init__(
            self,
            val,
            isLeaf,
            topLeft,
            topRight,
            bottomLeft,
            bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
