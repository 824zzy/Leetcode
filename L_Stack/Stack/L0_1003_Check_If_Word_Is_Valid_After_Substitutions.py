""" https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/
use stack to greedily find "abc" at the top
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            stk.append(c)
            while len(stk) >= 3 and stk[-3:] == ["a", "b", "c"]:
                stk.pop()
                stk.pop()
                stk.pop()

        return not stk
