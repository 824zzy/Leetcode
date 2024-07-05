""" https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
1. traverse from p to the root, store all the nodes
2. traverse from q to the root, find the first common node

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
from header import *


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        P = set()
        while p:
            P.add(p)
            p = p.parent
        while q:
            if q in P:
                return q
            q = q.parent


"""
[3,5,1,6,2,0,8,null,null,7,4]
5
1
[3,5,1,6,2,0,8,null,null,7,4]
5
4
[1,2]
1
2
"""
