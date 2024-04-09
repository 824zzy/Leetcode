""" https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/
solution1: from startIndex to targets
solution2: from targets to startIndex
"""
from header import *

# solution 1


class Solution:
    def closetTarget(self, A: List[str], t: str, s: int) -> int:
        ans = inf
        for i in range(s):
            if A[i] == t:
                ans = min(ans, s - i, len(A) - (s - i))

        for i in range(s, len(A)):
            if A[i] == t:
                ans = min(ans, i - s, len(A) - (i - s))
        return ans if ans != inf else -1

# solution 2


class Solution:
    def closetTarget(self, A: List[str], t: str, s: int) -> int:
        ans = inf
        for i in range(len(A)):
            if A[i] == t:
                ans = min(ans, abs(s - i), len(A) - abs(s - i))
        return ans if ans != inf else -1
