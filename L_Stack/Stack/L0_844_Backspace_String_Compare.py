""" https://leetcode.com/problems/backspace-string-compare/
scan s and t while check pound sign
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(s):
            stk = []
            for c in s:
                if c == '#':
                    if stk:
                        stk.pop()
                else:
                    stk.append(c)
            return stk
        return process(s) == process(t)
