""" https://leetcode.com/problems/nested-list-weight-sum/description/
dfs with depth
"""
from header import *

       
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(node, d):
            sm = 0
            for n in node:
                if n.isInteger():
                    sm += d*n.getInteger()
                else:
                    sm += dfs(n.getList(), d+1)
            return sm

        return dfs(nestedList, 1)
