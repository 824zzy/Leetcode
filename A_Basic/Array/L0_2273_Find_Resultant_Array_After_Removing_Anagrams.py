""" https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/
simulation
"""
from header import *


class Solution:
    def removeAnagrams(self, A: List[str]) -> List[str]:
        ans = [A[0]]
        for i in range(1, len(A)):
            if sorted(A[i]) != sorted(ans[-1]):
                ans.append(A[i])
        return ans
