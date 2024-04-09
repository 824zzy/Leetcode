""" https://leetcode.com/problems/determine-if-two-events-have-conflict/
only two cases:
AAAA
  BBBB
or
BBBB
  AAAA
"""
from header import *


class Solution:
    def haveConflict(self, A: List[str], B: List[str]) -> bool:
        if A[0] <= B[0] <= A[1] or B[0] <= A[0] <= B[1]:
            return True
        else:
            return False
