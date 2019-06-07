""" basic usage of recursive method
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.recursive(n, 0, "")
        return self.res
    
    def recursive(self, left, right, curr):
        if left == 0 and right == 0:
            self.res.append(curr)
        if left > 0:
            self.recursive(left-1, right+1, curr+"(")
        if right > 0:
            self.recursive(left, right-1, curr+")")