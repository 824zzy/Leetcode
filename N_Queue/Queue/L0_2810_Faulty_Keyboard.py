""" https://leetcode.com/problems/faulty-keyboard/
brute force or use deque
"""
from header import *


class Solution:
    def finalString(self, s: str) -> str:
        ans = ""
        for c in s:
            if c == "i":
                ans = ans[::-1]
            else:
                ans += c
        return ans


class Solution:
    def finalString(self, s: str) -> str:
        ans = deque()
        f = True
        for c in s:
            if c == "i":
                f = not f
            elif f:
                ans.append(c)
            else:
                ans.appendleft(c)
        return "".join(ans if f else reversed(ans))
