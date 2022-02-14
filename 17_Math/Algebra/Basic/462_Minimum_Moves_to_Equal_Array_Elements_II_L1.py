# Find the middle element as target
""" https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
In order to minimal the moves to make all elements equal, we need to find median as pivot.
"""
class Solution:
    def minMoves2(self, A: List[int]) -> int:
        t = sorted(A)[len(A)//2]
        ans = sum([abs(t-a) for a in A])
        return ans