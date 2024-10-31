""" https://leetcode.com/problems/find-the-original-typed-string-i/
use two pointers to keep track of the start and end of the same character
"""


class Solution:
    def possibleStringCount(self, A: str) -> int:
        A += "#"
        i = 0
        ans = 0
        for j in range(1, len(A)):
            if A[j] != A[j - 1]:
                ans += j - i - 1
                i = j
        return ans + 1
