""" https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/
1. The answer is true if t is greater or equal than the Chebyshev distance from (sx, sy) to (fx, fy). However, there is one more edge case to be considered.
2. The answer is false If sx == fx and sy == fy
"""
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        need = max(abs(sx-fx), abs(sy-fy))
        return t>=need if need else t!=1
        
"""
2
4
7
7
6
3
1
7
3
3
1
1
5
5
4
1
2
1
2
1
"""