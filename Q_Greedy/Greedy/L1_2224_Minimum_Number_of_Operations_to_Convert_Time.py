""" https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/
Since we can only add minutes, the greedy approach would work.
"""


class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        h0, m0 = current.split(":")
        h1, m1 = correct.split(":")
        h0, h1, m0, m1 = int(h0) * 60, int(h1) * 60, int(m0), int(m1)
        current, correct = h0 + m0, h1 + m1
        d = correct - current
        return d // 60 + d % 60 // 15 + d % 15 // 5 + d % 5
