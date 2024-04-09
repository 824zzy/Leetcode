""" https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/
for each bit position, find the maximum frequency of '1'
"""


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        A = []
        for i in range(24):
            cnt = 0
            for x in candidates:
                cnt += bool(x & 1 << i)
            A.append(cnt)
        return max(A)
