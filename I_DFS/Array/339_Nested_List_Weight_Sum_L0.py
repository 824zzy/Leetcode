""" https://leetcode.com/problems/nested-list-weight-sum/description/
dfs on NestedInteger
"""
from header import *

class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """
       
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
