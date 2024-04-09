""" https://leetcode.com/problems/escape-the-ghosts/
to escape, just check if you are closer to target than any ghost.
"""


class Solution:
    def escapeGhosts(self, A: List[List[int]], T: List[int]) -> bool:
        thres = abs(T[0]) + abs(T[1])
        return all([abs(i - T[0]) + abs(j - T[1]) > thres for i, j in A])
