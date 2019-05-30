""" easy problem
"""
class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        n = 0
        for each in S:
            if each in J:
                n = n + 1
        return n