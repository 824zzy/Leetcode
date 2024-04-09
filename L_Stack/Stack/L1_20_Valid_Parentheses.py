""" https://leetcode.com/problems/valid-parentheses/
use stack for simulation and map for brevity
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mp = {')': '(', '}': '{', ']': '['}
        for c in s:
            if c in '([{':
                stk.append(c)
            elif not stk or stk.pop() != mp[c]:
                return False
        return len(stk) == 0
