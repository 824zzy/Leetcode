""" https://leetcode.com/problems/longest-uncommon-subsequence-ii/
Observation: the longest uncommon subsequence is always the complete string itself, so just greedily consider all possible pairs of strings.

Since the data scale is small, just apply brute force simulation on all possible pairs of strings.

Time complexity: O(n^3)
"""

from header import *


class Solution:
    def findLUSlength(self, A: List[str]) -> int:
        def check(s1, s2):
            i = 0
            for j in range(len(s2)):
                if i < len(s1) and s1[i] == s2[j]:
                    i += 1
            return i == len(s1)

        A.sort(key=len, reverse=True)
        for i in range(len(A)):
            for j in range(len(A)):
                if i == j or len(A[i]) > len(A[j]):
                    continue
                if check(A[i], A[j]):
                    break
            else:
                return len(A[i])
        return -1


"""
["aba","cdc","eae"]
["aaa","aaa","aa"]
"""
