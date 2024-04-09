""" https://leetcode.com/problems/two-city-scheduling/
1. sort costs based on the difference of two entries.
2. greedily assign first half to A and second half to B
"""


class Solution:
    def twoCitySchedCost(self, A: List[List[int]]) -> int:
        A = sorted(A, key=lambda x: x[0] - x[1])
        ans = 0
        for i, (x, y) in enumerate(A):
            if i < len(A) // 2:
                ans += x
            else:
                ans += y
        return ans
